<script lang="ts">
	import type { SubmitFunction } from './$types';
	import { enhance } from '$app/forms';
	import { Button } from '$lib/components/ui/button';
	import { Label } from '$lib/components/ui/label';
	import { FieldContainer } from '$lib/components/layout/field-container';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { LoaderCircle } from 'lucide-svelte';
	import { toast } from 'svelte-sonner';
	import * as Alert from '$lib/components/ui/alert';
	import Sidebar from '../Sidebar.svelte';
	import AccountBanner from '../AccountBanner.svelte';
	import AccountFormSection from '../AccountFormSection.svelte';
	

	// Data
	let { data, form } = $props();

	// Form state
	let name = $state(
		data.account.first_name && data.account.last_name
			? `${data.account.first_name} ${data.account.last_name}`
			: ''
	);
	let email = $state(data.user.email || '');
	let isSubmitting: boolean = $state(false);
	let isSubmitted: boolean = $state(false);

	// Form submission
	const handleSubmit: SubmitFunction = () => {
		// Do something before the form is submitted (e.g. show a loader or validate the form)
		isSubmitting = true;

		return async ({ result, update }) => {
			// Do something after the form is submitted (e.g. hide a loader or show a success message)
			isSubmitting = false;
			isSubmitted = true;
			await update();

			toast.success('Support message has been successfully sent');

			// Reset the form to its initial state
			name =
				data.user.first_name && data.user.last_name
					? `${data.user.first_name} ${data.user.last_name}`
					: '';
			email = data.user.email || '';
		};
	};
</script>

<AccountBanner
	name={`${data.account.first_name} ${data.account.last_name}`}
	username={data.account.username}
	profileImageThumbnail={data.account.profile_image_thumbnail}
>
	<Button href="/profile" size="sm" variant="ghost">Return to profile</Button>
</AccountBanner>

<div class="py-6 sm:flex sm:gap-x-16">
	<aside class="overflow-hidden rounded-md border sm:w-48 sm:border-none md:w-64">
		<Sidebar />
	</aside>
	<div class="flex-1 space-y-12 pt-4 sm:pt-0">
		
		<form method="POST" action="?/submitSupportMessage" use:enhance={handleSubmit}>
			<AccountFormSection
				title="Support"
				description="Our support team will reach out to you at the earliest opportunity to assist with your request"
			/>

			<div class="mt-4 space-y-2 border-t border-gray-200 text-sm">
				<div class="grid grid-cols-6 gap-4 pt-4 md:grid-cols-12 md:gap-8">
					<FieldContainer class="col-span-6">
						<Label for="name">Name</Label>
						<Input type="text" id="name" name="name" maxlength={255} required bind:value={name} />
					</FieldContainer>

					<FieldContainer class="col-span-6">
						<Label for="email">Email address</Label>
						<Input type="email" id="email" name="email" maxlength={255} required bind:value={email} />
					</FieldContainer>
				</div>

				<FieldContainer class="pt-4">
					<Label for="subject">Subject</Label>
					<Input type="text" id="subject" name="subject" maxlength={255} required />
				</FieldContainer>

				<FieldContainer class="pt-4">
					<Label for="content">Message</Label>
					<Textarea id="content" name="content" maxlength={5000} required />
				</FieldContainer>
			</div>

			{#if isSubmitted}
				<Alert.Root class="mt-4 bg-green-50 text-green-800">
					<Alert.Title>Support message sent</Alert.Title>
					<Alert.Description>
						Your support message was successfully sent. Our team will reach out to you at the
						earliest opportunity to assist with your request.
					</Alert.Description>
				</Alert.Root>
			{:else}
				<div class="flex flex-row items-center justify-end gap-4 pt-4">
					{#if isSubmitting}
						<Button disabled variant="ghost" type="button">
							<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
							Sending message...
						</Button>
					{:else}
						<Button type="button" variant="ghost" size="sm">Cancel</Button>
						<Button type="submit" size="sm">Send message</Button>
					{/if}
				</div>
			{/if}
		</form>
	</div>
</div>
