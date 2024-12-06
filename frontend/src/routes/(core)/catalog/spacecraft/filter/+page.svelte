<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { MediaQuery } from 'runed';
	import * as Icons from '$lib/assets/product-icons/index';
	import { Separator } from '$lib/components/ui/separator';
	import { JsonCard } from '$lib/components/dev/json-card';

	let { data } = $props();

	const isDesktop = new MediaQuery('(min-width: 768px)');
	const count = 20;
	const perPage = $derived(isDesktop.matches ? 3 : 8);
	const siblingCount = $derived(isDesktop.matches ? 1 : 0);
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
			<Breadcrumb.Page>Spacecraft</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<div class="flex gap-6">
	<div class="flex-1 space-y-4">
		<!-- Header -->
		<div class="flex items-end justify-between">
			<div>
				<h2 class="text-lg font-medium">Categories</h2>
				<p class="text-muted text-nowrap text-sm font-medium">XX items</p>
			</div>
		</div>

		<!-- Grid listing -->
		<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
			{#if data.nodes.length > 0}
				{#each data.nodes as node}
					<div class="space-y-4 rounded-md p-4">
						<div>
							<h2 class="text-priamary text-lg font-medium">
								<a href="/catalog/spacecraft/filter/{node.slug}">{node.name}</a>
							</h2>
						</div>
						{#if node.children.length > 0}
							<Separator />
							<div class="-mt-4">
								{#each node.children as child}
									<a href="/catalog/spacecraft/filter/{child.slug}">
										<div class="group flex gap-x-6 rounded-md p-2 hover:bg-slate-50">
											<div>
												<img
													src={Icons.iconAcdsSs}
													alt="{child.name} category"
													class="h-12 w-12 rounded-md object-cover"
												/>
											</div>

											<div class="-mx-2 rounded-md">
												<h3 class="text-sm font-medium text-blue-600">{child.name}</h3>
												<p class="text-tertiary text-xs"># items</p>
											</div>
										</div>
									</a>
								{/each}
							</div>
						{/if}
					</div>
				{/each}
			{/if}
		</div>
	</div>
</div>

<JsonCard {data} isExpanded={true} />
