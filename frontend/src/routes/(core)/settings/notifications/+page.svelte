<script lang="ts">
	import { enhance } from '$app/forms';
	import { Button } from '$lib/components/ui/button';
	import { Label } from '$lib/components/ui/label';
	import { LoaderCircle } from 'lucide-svelte';
	import { toast } from 'svelte-sonner';

	import Sidebar from '../Sidebar.svelte';
	import AccountBanner from '../AccountBanner.svelte';
	import AccountFormSection from '../AccountFormSection.svelte';
	import { FieldContainerX } from '$lib/components/layout/field-container-x';
	import { Switch } from '$lib/components/ui/switch';
	import type { SubmitFunction } from './$types';
	import { JsonCard } from '$lib/components/dev/json-card';

	// Data
	let { data, form } = $props();

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);

	// Form submission
	function submitForm() {
		const formElm = document.getElementById('notifications-form') as HTMLFormElement | null;
		if (formElm) {
			formElm.requestSubmit();
		} else {
			console.error('Form element not found');
		}
	}

	const handleSubmit: SubmitFunction = () => {
		isSubmitting = true;

		return async ({ result, update }) => {
			// Do something after the form is submitted (e.g. hide a loader or show a success message)
			await update({ reset: false });
			isSubmitting = false;
			isSaved = true;


			console.log(form);
			console.log(result);
			console.log(data);

			try {
				await update({ reset: false });

				if (result.data.success === true) {
					toast.success('Notifications have been successfully updated');
				} else {
					toast.error('An error occurred, if the error persists please contact support');
				}

				console.log(result);
				console.log(data);

				// if (result.type === 'success') {
				// 	toast.success('Notifications have been successfully updated');
				// } else {
				// 	toast.error('An error occurred, if this problem persists please contact support');
				// }

				isSaved = true;
			} finally {
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
	<form
		method="POST"
		class="flex-1 space-y-12 pt-4 sm:pt-0"
		use:enhance={handleSubmit}
		id="notifications-form"
	>
		<div>
			<AccountFormSection title="Emails" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-marketing-emails">Marketing emails</Label>
						<div class="text-muted text-xs">Emails about promotions and discounts</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-marketing-emails"
							name="receive-marketing-emails"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_marketing_emails}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-weekly-digest-emails">Weekly digest</Label>
						<div class="text-muted text-xs">
							Receive weekly emails about website news and updates
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-weekly-digest-emails"
							name="receive-weekly-digest-emails"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_weekly_digest_emails}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-discovery-emails">Discovery emails</Label>
						<div class="text-muted text-xs">
							Receive emails about new components, features, tips, hints, and more
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-discovery-emails"
							name="receive-discovery-emails"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_discovery_emails}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-site-update-emails">Site updates</Label>
						<div class="text-muted text-xs">Receive important website changes and updates</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-site-update-emails"
							name="receive-site-update-emails"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_site_update_emails}
						/>
					</div>
				</FieldContainerX>
			</div>
		</div>

		<div>
			<AccountFormSection title="Notifications" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-inbox-message-notifications">Inbox messages</Label>
						<div class="text-muted text-xs">Get notified of new messages</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-inbox-message-notifications"
							name="receive-inbox-message-notifications"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_inbox_message_notifications}
						/>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="receive-announcement-notifications">Announcements</Label>
						<div class="text-muted text-xs">Receive announcement notifications</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Switch
							id="receive-announcement-notifications"
							name="receive-announcement-notifications"
							onclick={() => (isSaved = false)}
							checked={data.account.settings.receive_announcement_notifications}
						/>
					</div>
				</FieldContainerX>
			</div>
		</div>
	</form>
</div>

<JsonCard {data} />
