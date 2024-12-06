<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import SupplierCard from './SupplierCard.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';

	import { JsonCard } from '$lib/components/dev/json-card';
	import { page } from '$app/stores';

	let { data } = $props();

	// Create a reactive state for the query parameters
	let query = $derived($page.url.searchParams);

	let queryPageNumber = $derived(() => {
		const pageParam = query.get('page');
		const pageNumber = parseInt(pageParam || '1', 10); // Parse as an integer
		return isNaN(pageNumber) ? 1 : pageNumber; // Fallback to 1 if NaN
	});

	let queryFilter = $derived(() => {
		let params = new URLSearchParams(query);

		// Do a check to see if page is in the query parameters
		if (params.has('page')) {
			params.delete('page');
		}

		// Do a check to see if the query parameters are empty
		if (params.toString() === '') {
			return '';
		} else {
			return `&${params.toString()}`;
		}
	});

</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>Suppliers</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<div class="flex gap-6">
	<div class="flex-1 space-y-4">
		<div class="items-end md:flex md:justify-between">
			<div>
				<h2 class="text-lg font-medium">Suppliers</h2>
				<p class="text-muted text-nowrap text-sm font-medium">
					{#if data.pagination.total === 0}
						No suppliers found
					{:else if data.pagination.total === 1}
						{data.pagination.total} supplier found
					{:else}
						{data.pagination.total} suppliers found
					{/if}
				</p>
			</div>

			<div class="flex items-end gap-4 text-nowrap">
				<div class="flex w-full flex-row items-center gap-x-2">
					<Label for="supplier-search">Supplier search</Label>
					<Input
						type="text"
						id="supplier-search"
						name="supplier-search"
						placeholder="Search for supplier..."
					/>
				</div>
			</div>
		</div>

		<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			{#each data.suppliers as supplier}
				<SupplierCard {supplier} />
			{/each}
		</div>
	</div>
</div>

<JsonCard {data} isExpanded={true} />
