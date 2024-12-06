import json
import logging
import time
from collections import defaultdict
from typing import List, Optional

from apps.catalog.models import SpaceVehicleItem, Taxonomy, TaxonomyItem, TaxonomyNode
from apps.catalog.schemas import (
    GetTaxonomyNodeListSchema,
    GetTaxonomyNodeListWithChildrenSchema,
    GetTaxonomyNodeNestedListSchema,
    NestedTaxonomyNodeSchema,
    SpaceVehicleItemBasicSchema,
    TaxonomyItemSimpleSchema,
    TaxonomyNodeSchema,
    TaxonomyNodeWithChildrenSchema,
)
from apps.core.schemas import BaseResponseSchema
from apps.supplier.models import Supplier
from apps.supplier.schemas import SupplierBasicSchema
from django.db.models import Count, Prefetch
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Query, Schema
from pydantic import BaseModel

from .router import catalog_router


@catalog_router.get("/catalog/{taxonomy_slug}/filter-root-nodes")
def get_taxonomy_root_nodes(request: HttpRequest, taxonomy_slug: str):
    """
    Root views will not return items, only new views will return items.
    """
    logging.debug("[CATALOG.API] get_taxonomy_root_notes() Called")

    # Fetch the taxonomy
    taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)

    root_nodes = TaxonomyNode.objects.filter(taxonomy=taxonomy, parent=None)

    root_nodes_data = [TaxonomyNodeSchema.from_orm(node) for node in root_nodes]

    return 200, GetTaxonomyNodeListSchema(success=True, nodes=root_nodes_data)


@catalog_router.get("/catalog/{taxonomy_slug}/filter-root-nodes-and-children")
def get_taxonomy_root_nodes_and_children(request: HttpRequest, taxonomy_slug: str):
    """
    Root views will not return items, only new views will return items.
    """
    logging.debug("[CATALOG.API] get_taxonomy_root_notes() Called")

    # Fetch the taxonomy
    taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)

    # Fetch root nodes and prefetch their children
    root_nodes = TaxonomyNode.objects.filter(taxonomy=taxonomy, parent=None).prefetch_related("children")

    # Construct the response data
    root_nodes_data = []
    for node in root_nodes:
        node_data = NestedTaxonomyNodeSchema.from_orm(node).dict()  # Convert to a dictionary

        # Get's the immediate children of the node
        node_data["children"] = [TaxonomyNodeSchema.from_orm(child).dict() for child in node.children.all()]
        root_nodes_data.append(node_data)

    all_children_nodes_list = []

    # Return the response
    return 200, {
        "success": True,
        "message": "Request was successful",
        "nodes": root_nodes_data,
    }


# v1.2 get_taxonomy_nodes_with_children_and_items (allows filtering by supplier slug, made it return a single node and not a list of nodes)
# Reference: https://chatgpt.com/share/674827a8-6eb4-8013-89f2-b6b35f9f4ac1
# Reference: https://chatgpt.com/c/6747de47-02c4-8013-add4-d7d1118b7c57
@catalog_router.get("/catalog/{taxonomy_slug}/filter/{node_slug}")
def get_taxonomy_nodes_with_children_and_items(
    request: HttpRequest, taxonomy_slug: str, node_slug: str, supplier_slug: Optional[str] = None
):
    """
    Root views will return a single node with its immediate children and a list of all nodes with related items.
    """
    logging.debug("[CATALOG.API] get_taxonomy_root_notes() Called")

    # Fetch the taxonomy
    taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)

    # Fetch the root node and prefetch its immediate children
    root_node = TaxonomyNode.objects.filter(taxonomy=taxonomy, slug=node_slug).prefetch_related("children").first()

    if not root_node:
        return 404, {
            "success": False,
            "message": f"Node with slug '{node_slug}' not found in taxonomy '{taxonomy_slug}'.",
        }

    # Recursive function to gather all descendants
    def gather_all_nodes(node):
        nodes_list = [node]  # Start with the current node
        for child in node.children.all():
            nodes_list.extend(gather_all_nodes(child))  # Recursively gather all descendants
        return nodes_list

    # Gather all descendants (flat list of all nodes)
    all_children_nodes_list = gather_all_nodes(root_node)

    # Build nested data for the root node
    root_node_data = NestedTaxonomyNodeSchema.from_orm(root_node).dict()
    root_node_data["children"] = [TaxonomyNodeSchema.from_orm(child).dict() for child in root_node.children.all()]

    # Retrieve all related items for all nodes
    # Get relevant items based on the taxonomy type selected
    if taxonomy.slug == Taxonomy.TaxonomyChoices.SPACECRAFT:
        logging.debug("[CATALOG.API] get_taxonomy_nodes_with_children_and_items() - SPACECRAFT")
        related_items_query = SpaceVehicleItem.objects.filter(node__in=all_children_nodes_list).distinct()

        # Apply supplier_slug filter if provided
        if supplier_slug:
            related_items_query = related_items_query.filter(supplier__slug=supplier_slug)

        related_items_data = [SpaceVehicleItemBasicSchema.from_orm(item).dict() for item in related_items_query]

    elif taxonomy.slug == Taxonomy.TaxonomyChoices.LAUNCH_SITE:
        related_items_query = TaxonomyItem.objects.filter(node__in=all_children_nodes_list).distinct()
        related_items_data = [TaxonomyItemSimpleSchema.from_orm(item).dict() for item in related_items_query]

    elif taxonomy.slug == Taxonomy.TaxonomyChoices.LAUNCH_VEHICLE:
        related_items_query = TaxonomyItem.objects.filter(node__in=all_children_nodes_list).distinct()
        related_items_data = [TaxonomyItemSimpleSchema.from_orm(item).dict() for item in related_items_query]

    else:
        related_items_query = TaxonomyItem.objects.filter(node__in=all_children_nodes_list).distinct()
        related_items_data = [TaxonomyItemSimpleSchema.from_orm(item).dict() for item in related_items_query]

    # Return the response with a single root node and related items
    return 200, {
        "success": True,
        "message": "Request was successful",
        "node": root_node_data,  # Single root node with its immediate children
        "items": related_items_data,  # Related items for all nodes
    }


# v1.1 get_taxonomy_nodes_with_children_and_items (allows filtering by supplier slug)
# @catalog_router.get("/catalog/{taxonomy_slug}/filter/{node_slug}")
# def get_taxonomy_nodes_with_children_and_items(
#     request: HttpRequest, taxonomy_slug: str, node_slug: str, supplier_slug: Optional[str] = None
# ):
#     """
#     Root views will return nodes with their immediate children and a list of all nodes with related items.
#     """
#     logging.debug("[CATALOG.API] get_taxonomy_root_notes() Called")

#     # Fetch the taxonomy
#     taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)

#     # Fetch root nodes and prefetch their immediate children
#     root_nodes = TaxonomyNode.objects.filter(taxonomy=taxonomy, slug=node_slug).prefetch_related("children")

#     # Construct the nested nodes with immediate children
#     root_nodes_data = []
#     all_children_nodes_list = []  # To store all nodes (root + all descendants)

#     # Recursive function to gather all nodes
#     def gather_all_nodes(node):
#         nodes_list = [node]  # Start with the current node
#         for child in node.children.all():
#             nodes_list.extend(gather_all_nodes(child))  # Recursively gather all descendants
#         return nodes_list

#     # Loop through each root node
#     for node in root_nodes:
#         # Gather all descendants for the flat list
#         all_children_nodes_list.extend(gather_all_nodes(node))

#         # Build nested data for immediate children
#         node_data = NestedTaxonomyNodeSchema.from_orm(node).dict()
#         node_data["children"] = [TaxonomyNodeSchema.from_orm(child).dict() for child in node.children.all()]
#         root_nodes_data.append(node_data)

#     # Remove duplicates in all_children_nodes_list by converting to a set
#     all_children_nodes_list = list(set(all_children_nodes_list))

#     # Retrieve all related items for all nodes
#     related_items_query = TaxonomyItem.objects.filter(node__in=all_children_nodes_list).distinct()

#     # Apply supplier_slug filter if provided
#     if supplier_slug:
#         related_items_query = related_items_query.filter(supplier__slug=supplier_slug)

#     related_items_data = [TaxonomyItemSimpleSchema.from_orm(item).dict() for item in related_items_query]

#     # Return the response with nested nodes and flat list of items
#     return 200, {
#         "success": True,
#         "message": "Request was successful",
#         "nodes": root_nodes_data,  # Original nested nodes with immediate children
#         "items": related_items_data,  # Related items for all nodes
#     }


# v1.0 get_taxonomy_nodes_with_children_and_items
# Get all components and immediate children
# @catalog_router.get("/catalog/{taxonomy_slug}/filter/{node_slug}")
# def get_taxonomy_nodes_with_children_and_items(request: HttpRequest, taxonomy_slug: str, node_slug: str):
#     """
#     Root views will return nodes with their immediate children and a list of all nodes with related items.
#     """
#     logging.debug("[CATALOG.API] get_taxonomy_root_notes() Called")

#     # Fetch the taxonomy
#     taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)

#     # Fetch root nodes and prefetch their immediate children
#     root_nodes = TaxonomyNode.objects.filter(taxonomy=taxonomy, slug=node_slug).prefetch_related("children")

#     # Construct the nested nodes with immediate children
#     root_nodes_data = []
#     all_children_nodes_list = []  # To store all nodes (root + all descendants)

#     # Recursive function to gather all nodes
#     def gather_all_nodes(node):
#         nodes_list = [node]  # Start with the current node
#         for child in node.children.all():
#             nodes_list.extend(gather_all_nodes(child))  # Recursively gather all descendants
#         return nodes_list

#     # Loop through each root node
#     for node in root_nodes:
#         # Gather all descendants for the flat list
#         all_children_nodes_list.extend(gather_all_nodes(node))

#         # Build nested data for immediate children
#         node_data = NestedTaxonomyNodeSchema.from_orm(node).dict()
#         node_data["children"] = [TaxonomyNodeSchema.from_orm(child).dict() for child in node.children.all()]
#         root_nodes_data.append(node_data)

#     # Remove duplicates in all_children_nodes_list by converting to a set
#     all_children_nodes_list = list(set(all_children_nodes_list))

#     # Retrieve all related items for all nodes
#     related_items = TaxonomyItem.objects.filter(node__in=all_children_nodes_list).distinct()
#     related_items_data = [TaxonomyItemSimpleSchema.from_orm(item).dict() for item in related_items]

#     # Return the response with nested nodes and flat list of items
#     return 200, {
#         "success": True,
#         "message": "Request was successful",
#         "nodes": root_nodes_data,  # Original nested nodes with immediate children
#         "items": related_items_data,  # Related items for all nodes
#     }
