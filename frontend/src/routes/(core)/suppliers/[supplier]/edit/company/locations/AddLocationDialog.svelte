<script lang="ts">
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import * as Dialog from '$lib/components/ui/dialog';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
</script>

<Dialog.Root>
	<Dialog.Trigger>
		<Button size="sm">+ Add location</Button>
	</Dialog.Trigger>
	<Dialog.Content class="max-w-xl">
		<Dialog.Header>
			<Dialog.Title>Add new location</Dialog.Title>
		</Dialog.Header>
		<div class="grid grid-cols-12 gap-6 py-4">
			<FieldContainer class="col-span-8">
				<Label for="location-name">Location name</Label>
				<Input
					type="text"
					name="location-name"
					id="location-name"
					placeholder="New York Office"
					required
				/>
			</FieldContainer>
			<FieldContainer class="col-span-4">
				<Label for="location-type">Location type</Label>
				<Input type="text" name="location-type" id="location-type" required />
			</FieldContainer>

			<FieldContainer class="col-span-12">
				<Label for="address1">Address line 2</Label>
				<Input type="text" name="address1" id="address1" required />
			</FieldContainer>

			<FieldContainer class="col-span-12">
				<Label for="address2">Address line 2</Label>
				<Input type="text" name="address2" id="address2" required />
			</FieldContainer>

			<FieldContainer class="col-span-6">
				<Label for="city">City</Label>
				<Input type="text" name="city" id="city" required />
			</FieldContainer>

			<FieldContainer class="col-span-6">
				<Label for="subnational-region">State/Province/Region</Label>
				<Input type="text" name="subnational-region" id="subnational-region" required />
			</FieldContainer>

			<FieldContainer class="col-span-6">
				<Label for="country">Country</Label>
				<Input type="text" name="country" id="country" required />
			</FieldContainer>

			<FieldContainer class="col-span-6">
				<Label for="postal-code">Postal code</Label>
				<Input type="text" name="postal-code" id="postal-code" required />
			</FieldContainer>
		</div>

		<Dialog.Footer class="flex gap-2">
			<Dialog.Close class={buttonVariants({ variant: 'ghost', size: 'sm' })}>Cancel</Dialog.Close>
			<Button size="sm" type="submit">Add location</Button>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
