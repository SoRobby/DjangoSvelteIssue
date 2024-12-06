<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '$lib/components/ui/button';
	import { enhance } from '$app/forms';
	import type { SubmitFunction } from './$types';

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);

	const handleSubmit: SubmitFunction = () => {
		isSubmitting = true;

		// Append extra form data
		return async ({ result, update }) => {
			// Do something after the form is submitted (e.g. hide a loader or show a success message)
			isSubmitting = false;
			isSaved = true;

			await update({ reset: false });
		};
	};


</script>

<div class="space-y-12">
	<form method="POST" use:enhance={handleSubmit} id="profile-form">
		<section class="space-y-4">
			<div class="border-b pb-4">
				<SupplierFormSection
					title="SEO Information"
					description="Optimize your company's search engine presence"
				/>
			</div>
			<Button type="submit">
				Save changes
			</Button>
			<div class="grid grid-cols-12 gap-6">
				<FieldContainer class="col-span-12">
					<Label for="meta-title">Meta title</Label>
					<Input type="text" name="meta-title" id="meta-title" required />
				</FieldContainer>
				<FieldContainer class="col-span-12">
					<Label for="meta-description">Meta description</Label>
					<Textarea id="meta-description" name="meta-description"></Textarea>
				</FieldContainer>
				<FieldContainer class="col-span-12">
					<Label for="meta-keywords">Meta keywords</Label>
					<Input type="text" name="meta-keywords" id="meta-keywords" required />
				</FieldContainer>
			</div>
		</section>
	</form>
</div>
