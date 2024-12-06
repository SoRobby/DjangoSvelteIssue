<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
	let { data } = $props();
</script>

<div>
	<h2 class="text-primary pb-2 text-2xl font-bold">GET Request Examples</h2>
	<p class="text-tertiary">This is a short description of the dev page...</p>
</div>

<!-- Examples -->
<ComponentExample>
	<ComponentExample.Header>Server GET Request</ComponentExample.Header>
	<ComponentExample.Description>TBD</ComponentExample.Description>
	<ComponentExample.Preview>
		<div class="bg-muted mt-4 rounded-md p-2 text-xs">
			<div class="font-medium uppercase">Data</div>
			<pre>{JSON.stringify(data, null, 4)}</pre>
		</div>
	</ComponentExample.Preview>
</ComponentExample>
