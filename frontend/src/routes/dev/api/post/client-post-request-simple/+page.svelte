<script lang="ts">
	import { HelloWorldApi } from '$lib/api/client';
	import { ComponentExample } from '$lib/components/dev/component-example';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import * as Select from '$lib/components/ui/select';
	import { toast } from 'svelte-sonner';
	import { FieldContainer } from '$lib/components/layout/field-container';

	let { data } = $props();

	let content = $state('');
	let responseData = $state(null);
	let form: HTMLFormElement;

	async function handleSubmit(event: Event) {
		event.preventDefault();
		const data = await HelloWorldApi.helloWorldPost(content);

		if (!data.success) {
			console.log('[+PAGE.JS] Error response');
			toast.error('Request was unsuccessful');
			return data;
		} else {
			toast.success('Request was successful');
		}

		responseData = data;

		// Reset the form (optional)
		form.reset();
		return data;
	}
</script>

<div>
	<h2 class="text-primary pb-2 text-2xl font-bold">POST Request Examples</h2>
	<p class="text-tertiary">This is a short description of the dev page...</p>
</div>

<!-- Examples -->
<ComponentExample>
	<ComponentExample.Header>Client POST Request Simple</ComponentExample.Header>
	<ComponentExample.Description>TBD</ComponentExample.Description>
	<ComponentExample.Preview>
		<form bind:this={form} onsubmit={handleSubmit}>
			<div class="space-y-2">
				<FieldContainer>
					<Label for="content">Content</Label>
					<Input type="text" id="content" name="content" placeholder="Enter some text..." bind:value={content} />
				</FieldContainer>

				<Button variant="outline" size="sm" type="submit">Send POST Request</Button>
			</div>
		</form>

		<!-- Results -->
		<div class="bg-muted mt-4 rounded-md p-2 text-xs">
			<div class="font-medium uppercase">Data</div>
			<pre>{JSON.stringify(data, null, 4)}</pre>
		</div>

		<div class="bg-muted mt-4 rounded-md p-2 text-xs">
			<div class="font-medium uppercase">responseData</div>
			<pre>{JSON.stringify(responseData, null, 4)}</pre>
		</div>
	</ComponentExample.Preview>
</ComponentExample>
