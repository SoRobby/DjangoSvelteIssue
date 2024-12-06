<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import { Label } from '$lib/components/ui/label';
	import { ChevronLeft, ChevronRight, Box } from 'lucide-svelte';
	import * as Pagination from '$lib/components/ui/pagination';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import CatalogSidebar from './CatalogSidebar.svelte';
	import { MediaQuery } from 'runed';
	import GridItem from './GridItem.svelte';

	import { JsonCard } from '$lib/components/dev/json-card';

	let { data } = $props();

	const isDesktop = new MediaQuery('(min-width: 768px)');
	const count = 20;
	const perPage = $derived(isDesktop.matches ? 3 : 8);
	const siblingCount = $derived(isDesktop.matches ? 1 : 0);

	let selectedView = $state('grid-view');
	let selectedViewClone = $state('grid-view');
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/catalog">Catalog</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/catalog/spacecraft/filter">Spacecraft</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>{data.node.name}</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<div class="flex gap-6">
	<div class="md:64 hidden border-r pr-2 md:block lg:w-72">
		<div class="custom-scrollbar sticky top-0 z-30 h-screen overflow-y-auto">
			<CatalogSidebar />
		</div>
	</div>

	<div class="flex-1 space-y-4">
		<div class="flex items-end justify-between">
			<div>
				<h2 class="text-lg font-medium">{data.node.name}</h2>
				<p class="text-muted text-nowrap text-sm font-medium">
					{#if data.items.length === 0}
						No items found
					{:else if data.items.length === 1}
						{data.items.length} item
					{:else}
						{data.items.length} items
					{/if}
				</p>
			</div>

			{#if data.items.length > 0}
				<div class="flex items-end gap-4 text-nowrap">
					<div class="hidden flex-row items-center gap-x-2 md:flex">
						<Label for="supplier-search">Sort by</Label>
						<Select.Root type="single">
							<Select.Trigger class="w-44">Recently updated</Select.Trigger>
							<Select.Content>
								<Select.Item value="recently-updated">Recently updated</Select.Item>
								<Select.Item value="mass-low-to-high">Mass Low to High</Select.Item>
								<Select.Item value="mass-high-to-low">Mass High to Low</Select.Item>
							</Select.Content>
						</Select.Root>
					</div>
				</div>
			{/if}
		</div>

		<!-- If no items are found -->
		{#if data.items.length === 0}
			<div class="text-muted rounded-md border py-8 text-center">
				<Box size="36" class="mx-auto mb-2 opacity-50" />
				<p>No items found</p>
			</div>
		{:else}
			<!-- Grid listing -->
			{#if selectedView === 'grid-view'}
				<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
					{#each data.items as item}
						<GridItem
							itemName={item.name}
							itemSlug={item.slug}
							itemImage="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png"
							itemDryMass={item.properties?.dry_mass}
							itemPowerConsumption={item.properties?.power}
							itemIsFlightProven={item.is_flight_proven}
							itemDatasheet={false}
							itemCad={false}
							supplierName={item.supplier.name}
							supplierLogo="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png"
							supplierIsPremium={item.supplier.is_premium}
							showMenu={false}
						/>
					{/each}
				</div>
			{/if}

			<!-- Pagination -->
			<div>
				<Pagination.Root {count} {perPage} {siblingCount}>
					{#snippet children({ pages, currentPage })}
						<Pagination.Content>
							<Pagination.Item>
								<Pagination.PrevButton>
									<ChevronLeft class="size-4" />
									<span class="hidden sm:block">Previous</span>
								</Pagination.PrevButton>
							</Pagination.Item>
							{#each pages as page (page.key)}
								{#if page.type === 'ellipsis'}
									<Pagination.Item>
										<Pagination.Ellipsis />
									</Pagination.Item>
								{:else}
									<Pagination.Item>
										<Pagination.Link {page} isActive={currentPage === page.value}>
											{page.value}
										</Pagination.Link>
									</Pagination.Item>
								{/if}
							{/each}
							<Pagination.Item>
								<Pagination.NextButton>
									<span class="hidden sm:block">Next</span>
									<ChevronRight class="size-4" />
								</Pagination.NextButton>
							</Pagination.Item>
						</Pagination.Content>
					{/snippet}
				</Pagination.Root>
			</div>
		{/if}
	</div>
</div>

<JsonCard {data} isExpanded={true} />
