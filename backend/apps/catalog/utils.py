import json

from django.core import serializers


def generate_cached_properties(taxonomy_item, keys=None):
    """
    Generate a JSON representation of all properties associated with the TaxonomyItem.

    :param taxonomy_item: TaxonomyItem instance
    :param keys: Optional list of keys to include in the cached data
    :return: dict containing the cached properties
    """
    cached_data = {}

    # Fetch all related ItemProperty instances with their Property references
    item_properties = taxonomy_item.properties.select_related('property_reference').all()

    for item_property in item_properties:
        # Serialize the ItemProperty instance
        serialized_data = json.loads(serializers.serialize('json', [item_property]))[0]['fields']

        # Add additional fields from property_reference
        serialized_data['property_type'] = item_property.property_reference.property_type

        # Only add units_prefix and units_suffix for numeric property types
        # if item_property.property_reference.property_type in ['integer', 'float']:
        #     serialized_data['units_prefix'] = item_property.property_reference.units_prefix
        #     serialized_data['units_suffix'] = item_property.property_reference.units_suffix

        # Add the 'value' field
        serialized_data['value'] = item_property.value

        # If keys are provided, filter the serialized_data
        if keys:
            property_data = {k: serialized_data.get(k) for k in keys if k in serialized_data}
        else:
            property_data = serialized_data

        # Use the custom_key if available, otherwise use the property reference key
        cache_key = item_property.custom_key or item_property.property_reference.key

        cached_data[cache_key] = property_data

    return cached_data
