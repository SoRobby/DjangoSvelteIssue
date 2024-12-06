<script lang="ts">
	import type { HTMLAnchorAttributes } from 'svelte/elements';

	let { title, children }: HTMLAnchorAttributes & { title?: string } = $props();
</script>

<div class="space-y-2">
	{#if title}
		<h3 class="text-lg font-medium text-tertiary">{title}</h3>
	{/if}
	{@render children?.()}
</div>
