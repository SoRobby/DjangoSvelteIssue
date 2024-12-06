<script lang="ts">
	import { page } from '$app/stores';
	import type { Snippet } from 'svelte';

	let { children }: { children: Snippet } = $props();
</script>

<div class="flex gap-6 lg:gap-10">
	<aside class="hidden w-64 px-4 md:block">
		<!-- Design guidelines -->
		<div class="pb-4">
			<h4 class="mb-1 rounded-md py-1 text-sm font-medium">GET Requests</h4>
			<div class="grid grid-cols-1 text-sm">
				{@render sidebarLink('Client Get Request', '/dev/api/get/client-get-request')}
				{@render sidebarLink('Server Get Request', '/dev/api/get/server-get-request')}
			</div>
		</div>

		<!-- General Components -->
		<div class="pb-4">
			<h4 class="mb-1 rounded-md py-1 text-sm font-medium">POST Requests</h4>
			<div class="grid grid-cols-1 text-sm">
				{@render sidebarLink('Client Post Request Simple', '/dev/api/post/client-post-request-simple')}
				{@render sidebarLink('Server Post Request Simple', '/dev/api/post/server-post-request-simple')}
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
