<script lang="ts">
	let { title, description }: { title: string; description?: string } = $props();
</script>

<div>
	<h2 class="text-2xl font-semibold leading-7 text-primary">{title}</h2>
	{#if description}
		<p class="mt-2 text-sm leading-6 text-muted">
			{description}
		</p>
	{/if}
</div>



