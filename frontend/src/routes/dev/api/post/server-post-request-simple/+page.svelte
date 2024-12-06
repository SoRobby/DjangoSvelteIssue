<script lang="ts">
	import { HelloWorldApi } from '$lib/api/client';
	import { ComponentExample } from '$lib/components/dev/component-example';
	import type { SubmitFunction } from './$types';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import * as Select from '$lib/components/ui/select';
	import { toast } from 'svelte-sonner';
	import { applyAction, enhance } from '$app/forms';
	import { FieldContainer } from '$lib/components/layout/field-container';

	let { data, form } = $props();
	let content = $state('');
	let isSubmitting = $state(false);

	const handleSubmit: SubmitFunction = () => {
		isSubmitting = true;

		return async ({ result, update }) => {
			try {
				await update();
				if ('data' in result && result.data?.success) {
					toast.success('Request was successful');
				} else {
					toast.error('Unable to process request');
				}
			} catch (error) {
				toast.error('An error occurred');
			} finally {
				isSubmitting = false;
			}

			await applyAction(result);
			console.log('result: ', result);
			console.log('form: ', form);
		};
	};
</script>

<div>
	<h2 class="text-primary pb-2 text-2xl font-bold">POST Request Examples</h2>
	<p class="text-tertiary">This is a short description of the dev page...</p>
</div>

<!-- Examples -->
<ComponentExample>
	<ComponentExample.Header>Server POST Request Simple</ComponentExample.Header>
	<ComponentExample.Description>TBD</ComponentExample.Description>
	<ComponentExample.Preview>

		<Input type="text" id="search" name="search" placeholder="Search..." />
		
		<form method="POST" use:enhance={handleSubmit}>
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
			<div class="font-medium uppercase">Form</div>
			<pre>{JSON.stringify(form, null, 4)}</pre>
		</div>
	</ComponentExample.Preview>
</ComponentExample>
