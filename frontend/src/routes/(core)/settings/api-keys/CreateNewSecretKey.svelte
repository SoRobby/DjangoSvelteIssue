<script lang="ts">
	import { Button, buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';

	// API key generation state
	let isApiKeyGenerated = $state(false);
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants({ size: 'sm' })}>+ Create new secret key</Dialog.Trigger>
	<Dialog.Content escapeKeydownBehavior="ignore" interactOutsideBehavior="ignore">
		{#if !isApiKeyGenerated}
			<Dialog.Header>
				<Dialog.Title>Create new secret key</Dialog.Title>
				<Dialog.Description>
					This action cannot be undone. This will permanently delete your account and remove your
					data from our servers.
				</Dialog.Description>
			</Dialog.Header>
			<div class="space-y-4 py-4">
				<FieldContainer>
					<Label for="name">Name</Label>
					<Input type="text" name="name" id="name" required placeholder="My Test API Key" />
				</FieldContainer>
			</div>
			<Dialog.Footer class="flex gap-x-2">
				<Dialog.Close class={buttonVariants({ variant: 'outline', size: 'sm' })}
					>Cancel</Dialog.Close
				>
				<Button type="submit" size="sm" onclick={() => (isApiKeyGenerated = true)}
					>Create secret key</Button
				>
			</Dialog.Footer>
		{:else}
			<Dialog.Header>
				<Dialog.Title>Save your key</Dialog.Title>
				<Dialog.Description>
					Please save this secret key somewhere safe and accessible. For security reasons, <strong
						>you won't be able to view it again</strong
					> through your account. If you lose this secret key, you'll need to generate a new one.
				</Dialog.Description>
			</Dialog.Header>
			<div class="space-y-4 py-4">
				<FieldContainer>
					<Input
						type="text"
						id="secret-key"
						value="placeholder..."
						readonly
					/>
				</FieldContainer>
			</div>
			<Dialog.Footer class="flex gap-x-2">
				<Dialog.Close class={buttonVariants({ variant: 'outline', size: 'sm' })}>Done</Dialog.Close>
			</Dialog.Footer>
		{/if}
	</Dialog.Content>
</Dialog.Root>
