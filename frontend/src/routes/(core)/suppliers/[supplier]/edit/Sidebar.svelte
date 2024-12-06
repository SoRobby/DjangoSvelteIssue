<script lang="ts">
	import { page } from '$app/stores';

	let { supplierSlug }: { supplierSlug: string } = $props();
</script>

<nav class="flex-none space-y-8">
	<div>
		<ul role="list" class="gap-x-3 gap-y-1 whitespace-nowrap pr-4 lg:flex-col">
			{@render sidebarItem('Dashboard', `/suppliers/${supplierSlug}/edit`)}
		</ul>
	</div>

	<div>
		<h2 class="pl-2 text-xs font-medium text-gray-600">Company</h2>
		<ul role="list" class="mt-1 gap-x-3 gap-y-1 whitespace-nowrap pr-4 lg:flex-col">
			{@render sidebarItem('Profile', `/suppliers/${supplierSlug}/edit/company/profile`)}
			{@render sidebarItem('Locations', `/suppliers/${supplierSlug}/edit/company/locations`)}
			{@render sidebarItem('SEO', `/suppliers/${supplierSlug}/edit/company/seo`)}
		</ul>
	</div>

	<div>
		<h2 class="pl-2 text-xs font-medium text-gray-600">Products & Services</h2>
		<ul role="list" class="mt-1 gap-x-3 gap-y-1 whitespace-nowrap pr-4 lg:flex-col">
			{@render sidebarItem('Products', `/suppliers/${supplierSlug}/edit/products`)}
			{@render sidebarItem('Services', `/suppliers/${supplierSlug}/edit/services`)}
		</ul>
	</div>

	<div>
		<h2 class="pl-2 text-xs font-medium text-gray-600">Settings</h2>
		<ul role="list" class="mt-1 gap-x-3 gap-y-1 whitespace-nowrap pr-4 lg:flex-col">
			{@render sidebarItem('User Management', `/suppliers/${supplierSlug}/edit/settings/users`)}
			{@render sidebarItem('Region Control', `/suppliers/${supplierSlug}/edit/settings/region-control`)}
		</ul>
	</div>

	<div>
		<h2 class="pl-2 text-xs font-medium text-gray-600">Support</h2>
		<ul role="list" class="mt-1 gap-x-3 gap-y-1 whitespace-nowrap pr-4 lg:flex-col">
			{@render sidebarItem('Contact Support', `/suppliers/${supplierSlug}/edit/help/contact`)}
			{@render sidebarItem('FAQ', `/suppliers/${supplierSlug}/edit/help/faq`)}
		</ul>
	</div>
</nav>

{#snippet sidebarItem(name: string, href: string)}
	<li>
		{#if $page.url.pathname === href}
			<a
				{href}
				class="text-brand flex gap-x-3 rounded-md bg-gray-100 py-1.5 pl-2 text-sm font-medium"
			>
				{name}
			</a>
		{:else}
			<a
				{href}
				class="text-tertiary flex gap-x-3 rounded-md py-1.5 pl-2 text-sm hover:bg-gray-50 hover:text-secondary"
			>
				{name}
			</a>
		{/if}
	</li>
{/snippet}
