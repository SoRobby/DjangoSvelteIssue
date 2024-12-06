<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import { Label } from '$lib/components/ui/label';
	import * as Pagination from '$lib/components/ui/pagination';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { Input } from '$lib/components/ui/input';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import RequestInfoForm from './RequestInfoForm.svelte';
	import * as Avatar from '$lib/components/ui/avatar';
	import { smoothScrollTo } from '$lib/utils';
	import {
		ChevronDown,
		ChevronRight,
		Info,
		FileText,
		StickyNote,
		Download,
		ArrowRightFromLine
	} from 'lucide-svelte';

	import * as Tooltip from '$lib/components/ui/tooltip';

	let { item } = $props();
</script>

<div>
	<h4 class="text-sm font-medium">Overview</h4>
	<dl class="divide-y divide-gray-100">
		<div class="grid grid-cols-2 py-3">
			<dt class="text-muted text-sm font-medium">Name</dt>
			<dd class="text-muted text-sm">{item.name}</dd>
		</div>
		<div class="grid grid-cols-2 py-3">
			<dt class="text-muted text-sm font-medium">Supplier</dt>
			<dd class="text-muted text-sm">{item.supplier.name}</dd>
		</div>
		<div class="grid grid-cols-2 py-3">
			<dt class="text-muted text-sm font-medium">Type</dt>
			<dd class="text-muted text-sm">{item.node.name}</dd>
		</div>
		<div class="grid grid-cols-2 py-3">
			<dt class="text-muted text-sm font-medium">Flight proven</dt>
			<dd class="text-muted text-sm">{item.is_flight_proven ? 'Yes' : 'No'}</dd>
		</div>
	</dl>
</div>

<div>
	<h4 class="text-sm font-medium">Details</h4>
	<dl class="divide-y divide-gray-100">
		{#each item.properties as property}
			<div class="grid grid-cols-2 py-3">
				<dt class="text-muted text-sm font-medium">{property.property_definition.name}</dt>

				<dd class="text-muted flex items-center justify-between pr-4 text-sm">
					{#if property.property_definition.property_type === 'integer'}
						{property.integer_value}
						{#if property.property_definition.details.units_suffix}
							{property.property_definition.details.units_suffix}
						{/if}
					{:else if property.property_definition.property_type === 'float'}
						{property.float_value}
						{#if property.property_definition.details.units_suffix}
							{property.property_definition.details.units_suffix}
						{/if}
					{:else if property.property_definition.property_type === 'string'}
						{property.string_value}
					{:else if property.property_definition.property_type === 'boolean'}
						{property.boolean_value ? 'Yes' : 'No'}
					{/if}

					{#if property.note}
						<Tooltip.Provider delayDuration={100} disableCloseOnTriggerClick={true}>
							<Tooltip.Root>
								<Tooltip.Trigger class={buttonVariants({ variant: 'ghost', size: 'none' })}>
									<Info class="h-4 w-4" />
								</Tooltip.Trigger>
								<Tooltip.Content class="max-w-64">
									<p>{property.note}</p>
								</Tooltip.Content>
							</Tooltip.Root>
						</Tooltip.Provider>
					{/if}
				</dd>
			</div>
		{/each}
	</dl>
</div>

<!-- <div>
    <h4 class="text-sm font-medium">Mechanical</h4>
    <dl class="divide-y divide-gray-100">
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Dry mass</dt>
            <dd class="text-muted text-sm">1.24 kg</dd>
        </div>
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Dimensions</dt>
            <dd class="text-muted flex items-center justify-between pr-4 text-sm">
                <span> 120 x 200 x 50 mm</span>

                <div class="flex items-center gap-x-4">
                    <Tooltip.Provider delayDuration={100} disableCloseOnTriggerClick={true}>
                        <Tooltip.Root>
                            <Tooltip.Trigger class={buttonVariants({ variant: 'ghost', size: 'none' })}>
                                <Info class="h-4 w-4" />
                            </Tooltip.Trigger>
                            <Tooltip.Content>
                                <p>Add to library</p>
                            </Tooltip.Content>
                        </Tooltip.Root>
                    </Tooltip.Provider>

                    <Tooltip.Provider delayDuration={100} disableCloseOnTriggerClick={true}>
                        <Tooltip.Root>
                            <Tooltip.Trigger class={buttonVariants({ variant: 'ghost', size: 'none' })}>
                                <FileText class="h-4 w-4" />
                            </Tooltip.Trigger>
                            <Tooltip.Content>
                                <p>Add to library</p>
                            </Tooltip.Content>
                        </Tooltip.Root>
                    </Tooltip.Provider>

                    <Tooltip.Provider delayDuration={100} disableCloseOnTriggerClick={true}>
                        <Tooltip.Root>
                            <Tooltip.Trigger class={buttonVariants({ variant: 'ghost', size: 'none' })}>
                                <StickyNote class="w-4" />
                            </Tooltip.Trigger>
                            <Tooltip.Content>
                                <p>Add to library</p>
                            </Tooltip.Content>
                        </Tooltip.Root>
                    </Tooltip.Provider>
                </div>
            </dd>
        </div>
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Full name</dt>
            <dd class="text-muted text-sm">Margot Foster</dd>
        </div>
    </dl>
</div>

<div>
    <h4 class="text-sm font-medium">Power</h4>
    <dl class="divide-y divide-gray-100">
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Full name</dt>
            <dd class="text-muted text-sm">Margot Foster</dd>
        </div>
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Full name</dt>
            <dd class="text-muted text-sm">Margot Foster</dd>
        </div>
        <div class="grid grid-cols-2 py-3">
            <dt class="text-muted text-sm font-medium">Full name</dt>
            <dd class="text-muted text-sm">Margot Foster</dd>
        </div>
    </dl>
</div> -->
