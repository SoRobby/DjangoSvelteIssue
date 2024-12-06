<script lang="ts">
	import { page } from '$app/stores';
</script>

<nav class="flex-none">
	<ul role="list" class="gap-x-3 gap-y-1 whitespace-nowrap lg:flex-col">
		{@render sidebarItem('General', '/settings/general')}
		{@render sidebarItem('Notifications', '/settings/notifications')}
		{@render sidebarItem('API Keys', '/settings/api-keys')}
		{@render sidebarItem('Security', '/settings/security')}
		{@render sidebarItem('Support', '/settings/support')}

		<hr class="mt-4 pb-4" />

		{@render sidebarItem('Admin panel', '/')}
		{@render sidebarItem('Django panel', '/')}
	</ul>
</nav>

{#snippet sidebarItem(name: string, href: string)}
	<li>
		{#if $page.url.pathname === href}
			<a
				{href}
				class="text-brand flex gap-x-3 rounded-md bg-gray-100 py-2 pl-2 pr-3 text-sm font-semibold leading-6"
			>
				{name}
			</a>
		{:else}
			<a
				{href}
				class="text-tertiary flex gap-x-3 rounded-md py-2 pl-2 pr-3 text-sm font-semibold leading-6 hover:bg-gray-50 hover:text-secondary"
			>
				{name}
			</a>
		{/if}
	</li>
{/snippet}
