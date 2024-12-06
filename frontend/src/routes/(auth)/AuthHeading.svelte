<script lang="ts">
	import { PUBLIC_SITE_NAME } from '$env/static/public';

	const {
		title
	}: {
		title?: string;
	} = $props();
</script>

<div class="flex flex-col items-center justify-center sm:mx-auto sm:w-full sm:max-w-md">
	<a href="/" class="flex items-center gap-x-2 text-lg font-medium">
		{PUBLIC_SITE_NAME}
	</a>
	{#if title}
		<h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
			{title}
		</h2>
	{/if}
</div>
