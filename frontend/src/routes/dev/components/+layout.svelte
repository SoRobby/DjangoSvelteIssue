<script lang="ts">
	import { page } from '$app/stores';
	import type { Snippet } from 'svelte';

	let { children }: { children: Snippet } = $props();
</script>

<div class="flex gap-6 lg:gap-10">
	<aside class="hidden w-64 px-4 md:block">
		<!-- Design guidelines -->
		<div class="pb-4">
			<h4 class="mb-1 rounded-md py-1 text-sm font-medium">Design Guidelines</h4>
			<div class="grid grid-cols-1 text-sm">
				{@render sidebarLink('All elements', '/dev/components/all-elements')}
				{@render sidebarLink('Colors', '/dev/components/colors')}
			</div>
		</div>

		<!-- General Components -->
		<div class="pb-4">
			<h4 class="mb-1 rounded-md py-1 text-sm font-medium">General Components</h4>
			<div class="grid grid-cols-1 text-sm">
				{@render sidebarLink('Hello', '/hello')}
				{@render sidebarLink('Badge', '/dev/components/badge')}
				{@render sidebarLink('Button', '/dev/components/button')}
			</div>
		</div>

		<!-- App specific components -->
		<div class="pb-4">
			<h4 class="mb-1 rounded-md py-1 text-sm font-medium">App Components</h4>
			<div class="grid grid-cols-1 text-sm">
				{@render sidebarLink('Hello', '/hello')}
			</div>
		</div>
	</aside>

	<section class="flex-1 px-4">
		{@render children()}
	</section>
</div>

{#snippet sidebarLink(name: string, href: string)}
	{#if $page.url.pathname === href}
		<a {href} class="flex items-center rounded-md bg-muted px-2 py-1 text-primary">{name}</a>
	{:else}
		<a
			{href}
			class="flex items-center rounded-md px-2 py-1 text-tertiary hover:bg-muted hover:text-secondary hover:underline"
			>{name}</a
		>
	{/if}
{/snippet}
