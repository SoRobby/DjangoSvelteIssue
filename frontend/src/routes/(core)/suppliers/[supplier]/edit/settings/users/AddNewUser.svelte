<script lang="ts">
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import * as Dialog from '$lib/components/ui/dialog';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import * as Alert from '$lib/components/ui/alert';
	import { Info } from 'lucide-svelte';
</script>

<Dialog.Root>
	<Dialog.Trigger>
		<Button size="sm">+ Add user</Button>
	</Dialog.Trigger>
	<Dialog.Content id="dialog-content" class="max-w-lg">
		<Dialog.Header>
			<Dialog.Title>Add new user</Dialog.Title>
		</Dialog.Header>
		<div class="space-y-4 py-4">
			<FieldContainer>
				<Label for="email">Email address</Label>
				<Input type="email" name="email" id="email" required placeholder="Enter email address" />
			</FieldContainer>

			<Alert.Root class="border-blue-200 bg-blue-50 text-sm">
				<Info class="h-4 w-4 text-blue-400" />
				<Alert.Title class="text-blue-800">About adding a user</Alert.Title>
				<Alert.Description class="text-blue-700">
					For security purposes, only accounts that are already registered on the platform can be
					added.</Alert.Description
				>
			</Alert.Root>
		</div>
		<Dialog.Footer class="flex gap-2">
			<Dialog.Close class={buttonVariants({ variant: 'ghost', size: 'sm' })}>Cancel</Dialog.Close>
			<Button size="sm" type="submit">Send invitation</Button>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
