<script lang="ts">
	import Sidebar from '../Sidebar.svelte';
	import AccountBanner from '../AccountBanner.svelte';
	import { Button } from '$lib/components/ui/button';
	import AccountFormSection from '../AccountFormSection.svelte';
	import { Label } from '$lib/components/ui/label';
	import { FieldContainerX } from '$lib/components/layout/field-container-x';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { LoaderCircle } from 'lucide-svelte';
	import CountrySelect from './CountrySelect.svelte';
	import { JsonCard } from '$lib/components/dev/json-card';
	import { toast } from 'svelte-sonner';
	import { enhance } from '$app/forms';
	import type { SubmitFunction } from './$types';

	// Data
	let { data } = $props();

	// Form state
	let firstName = $state(data.account.first_name);
	let lastName = $state(data.account.last_name);
	let bio = $state(data.account.bio);
	let organization = $state(data.account.organization);
	let position = $state(data.account.position);
	let countrySlug = $state(data.account.country.slug);

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);

	function submitForm() {
		const formElm = document.getElementById('profile-form') as HTMLFormElement | null;
		if (formElm) {
			formElm.requestSubmit();
		} else {
			console.error('Form element not found');
		}
	}

	const handleSubmit: SubmitFunction = ({ formData }) => {
		isSubmitting = true;

		// Append extra form data
		formData.append('countrySlug', countrySlug?.toString() || '');

		return async ({ result, update }) => {
			// Do something after the form is submitted (e.g. hide a loader or show a success message)
			isSubmitting = false;
			isSaved = true;
			await update({ reset: false });

			try {
				if (result.type === 'success') {
					if (result.data && result.data.success === true) {
						await update({ reset: false });
						toast.success('Notifications have been successfully updated');
					} else {
						toast.error('An error occurred, if the error persists please contact support');
					}
				} else {
					toast.error('An error occurred, if the error persists please contact support');
				}

				console.log(result);
				console.log(data);
			} finally {
				isSaved = true;
				isSubmitting = false;
			}
		};
	};
</script>

<AccountBanner
	name={`${data.account.first_name} ${data.account.last_name}`}
	username={data.account.username}
	profileImageThumbnail={data.account.profile_image_thumbnail}
>
	{#if isSaved}
		<Button href="/profile" size="sm" variant="ghost">Return to profile</Button>
	{:else if isSubmitting}
		<Button disabled variant="ghost" type="button">
			<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
			Saving...
		</Button>
	{:else}
		<Button href="/profile" size="sm" variant="ghost">Cancel</Button>
		<Button type="button" size="sm" onclick={submitForm}>Save changes</Button>
	{/if}
</AccountBanner>

<div class="py-6 sm:flex sm:gap-x-16">
	<aside class="overflow-hidden rounded-md border sm:w-48 sm:border-none md:w-64">
		<Sidebar />
	</aside>
	<div class="flex-1 space-y-12 pt-4 sm:pt-0">
		<form method="POST" use:enhance={handleSubmit} id="profile-form">
			<AccountFormSection title="Profile" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label>Username</Label>
						<div class="text-muted text-xs">Username is public and cannot be changed</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						{data.account.username}
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="first-name">First name</Label>
						<div class="text-muted text-xs">
							Your name remains private unless you set your privacy to public
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<Input
							type="text"
							name="first-name"
							id="first-name"
							class="max-w-full"
							maxlength={120}
							required
							onkeydown={() => (isSaved = false)}
							bind:value={firstName}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="last-name">Last name</Label>
						<div class="text-muted text-xs">
							Your name remains private unless you set your privacy to public
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<Input
							type="text"
							name="last-name"
							id="last-name"
							class="max-w-full"
							maxlength={120}
							required
							onkeydown={() => (isSaved = false)}
							bind:value={lastName}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="country">Profile picture</Label>
						<div class="text-muted text-xs">
							Upload a png, jpg up to 5 MB (recommended size 500 x 500 px)
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						Coming soon....
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="bio">About you</Label>
						<div class="text-muted text-xs">A short description of you and your expertise</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<Textarea
							name="bio"
							id="bio"
							placeholder="Example: Spacecraft systems engineer at..."
							maxlength={1000}
							onkeydown={() => (isSaved = false)}
							bind:value={bio}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="organization">Organization</Label>
						<div class="text-muted text-xs">Your affiliated organization, company, or school</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<Input
							type="text"
							name="organization"
							id="organization"
							class="max-w-full"
							maxlength={255}
							onkeydown={() => (isSaved = false)}
							bind:value={organization}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="position">Position / Role</Label>
						<div class="text-muted text-xs">
							Role or position at your organization, company, or school
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<Input
							type="text"
							name="position"
							id="position"
							class="max-w-full"
							maxlength={255}
							onkeydown={() => (isSaved = false)}
							bind:value={position}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="country">Country</Label>
						<div class="text-muted text-xs">Country of residence</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						<CountrySelect
							countries={data.countries}
							selectedCountrySlug={data.account.country.slug}
							onSelect={(selectedSlug: string) => {
								countrySlug = selectedSlug; // Update the `country` state
								isSaved = false; // Mark the form as unsaved
							}}
						/>
					</div>
				</FieldContainerX>
			</div>
		</form>

		<div>
			<AccountFormSection title="Metrics" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX class="items-center">
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label>Member since</Label>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-start">
						Coming soon.... (e.g., July 7, 2020)
					</div>
				</FieldContainerX>
			</div>
		</div>
	</div>
</div>

<JsonCard {data} />
