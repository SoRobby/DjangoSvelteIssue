<script lang="ts">
	import type { HTMLAnchorAttributes } from 'svelte/elements';
	let { title, children }: HTMLAnchorAttributes & { title: string } = $props();
</script>

<section class="space-y-4 border-x border-dashed px-6 py-4 text-tertiary">
	<h2 class="border-b py-2 text-2xl font-medium text-secondary">{title}</h2>
	{@render children?.()}
</section>
