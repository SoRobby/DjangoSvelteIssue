<script lang="ts">
	import type { Snippet } from 'svelte';
	import * as Avatar from '$lib/components/ui/avatar';

	let {
		name,
		username,
		profileImageThumbnail,
		children
	}: { name: string; username: string; profileImageThumbnail?: string; children?: Snippet } =
		$props();
</script>

<div class="py-4 sm:flex sm:items-center sm:py-6">
	<div class="flex flex-1 items-center space-x-4">
		<div>
			<Avatar.Root class="h-12 w-12">
				{#if profileImageThumbnail}
					<Avatar.Image src={profileImageThumbnail} alt="@{username}" />
				{:else}
					<Avatar.Fallback>
						{username.slice(0, 2).toUpperCase()}
					</Avatar.Fallback>
				{/if}
			</Avatar.Root>
		</div>
		<div>
			<h1 class="text-primary text-2xl font-semibold">{name}</h1>
			<p class="text-muted text-sm font-medium">@{username}</p>
		</div>
	</div>
	{#if children}
		<div class="space-x-4">
			{@render children()}
		</div>
	{/if}
</div>
