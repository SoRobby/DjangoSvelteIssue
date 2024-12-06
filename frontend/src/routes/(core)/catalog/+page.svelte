<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { JsonCard } from '$lib/components/dev/json-card';

	let { data } = $props();
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>Catalog</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
	{@render CatalogCard(
		'Products',
		'Description of product catalog...',
		'/catalog/spacecraft'
	)}
</div>

<JsonCard {data} isExpanded={true} />

{#snippet CatalogCard(name: string, description: string, href: string)}
	<div class="relative rounded-md border p-4 hover:bg-slate-50">
		<h2 class="text-primary text-lg font-medium">{name}</h2>
		<p class="text-tertiary">{description}</p>
		<a {href} class="absolute inset-0 block" aria-hidden="true">
			<span aria-hidden="true"></span>
		</a>
	</div>
{/snippet}
