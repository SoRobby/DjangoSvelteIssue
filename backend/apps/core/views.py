import time

from apps.catalog.models import SpaceVehicleItem, TaxonomyItem
from apps.properties.models import Property
from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}

    properties = Property.objects.all()

    space_vehicle_items = SpaceVehicleItem.objects.all()


    start_time = time.time()
    taxonomy_items = TaxonomyItem.objects.filter(
        properties__property_definition__key='dry_mass',
        properties__float_value__gt=1
    ).distinct()

    end_time = time.time()
    print(f'Query time = {end_time - start_time} seconds')

    print(f'taxonomy_items = {taxonomy_items}')

    # cached_props = generate_cached_properties(space_vehicle_items[0])
    # cached_props2 = space_vehicle_items[0].update_cached_properties()
    # cached_props3 = space_vehicle_items[0].update_cached_properties2()
    # cached_props4 = space_vehicle_items[0].update_cached_properties3()
    # print(f'\ncached_props = {cached_props}')
    # print(f'\ncached_props2 = {cached_props2}')
    # print(f'\ncached_props3 = {cached_props3}')
    # print(f'\ncached_props4 = {cached_props4}')

    context['space_vehicle_items'] = space_vehicle_items
    context['properties'] = properties

    return render(request, 'core/home.html', context)



