<script lang="ts">
	import SupplierBanner from './SupplierBanner.svelte';
	import { Button } from '$lib/components/ui/button';
	import { LoaderCircle } from 'lucide-svelte';
	import Sidebar from './Sidebar.svelte';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import JsonCard from '$lib/components/dev/json-card/json-card.svelte';

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);
	let { data, children } = $props();
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/suppliers">Suppliers</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/suppliers/{data.supplier.slug}">{data.supplier.name}</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>Edit</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<SupplierBanner supplier={data.supplier}>
	{#if isSaved}
		<Button href="/" size="sm" variant="ghost">Return to profile</Button>
	{:else if isSubmitting}
		<Button disabled variant="ghost" type="button">
			<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
			Saving...
		</Button>
	{:else}
		<Button href="/profile" size="sm" variant="ghost">Cancel</Button>
		<Button href="/profile" size="sm">Save changes</Button>
	{/if}
</SupplierBanner>

<div class="py-6 sm:flex sm:gap-x-8">
	<aside class="overflow-hidden border-r sm:w-48 md:w-56">
		<Sidebar supplierSlug={data.supplier.slug} />
	</aside>
	<div class="flex-1 space-y-12 pt-4 sm:pt-0">
		{@render children()}
	</div>
</div>

<JsonCard {data} isExpanded={true} />
