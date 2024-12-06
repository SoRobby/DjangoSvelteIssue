<script lang="ts">
	import Sidebar from '../Sidebar.svelte';
	import AccountBanner from '../AccountBanner.svelte';
	import { Button } from '$lib/components/ui/button';
	import AccountFormSection from '../AccountFormSection.svelte';
	import { Label } from '$lib/components/ui/label';
	import { FieldContainerX } from '$lib/components/layout/field-container-x';
	import { LoaderCircle } from 'lucide-svelte';
    import { Badge } from "$lib/components/ui/badge";
	import DeleteAccountDialog from './DeleteAccountDialog.svelte';

	// Data
	let { data } = $props();

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);
</script>

<AccountBanner name={`${data.account.first_name} ${data.account.last_name}`} username={data.account.username} profileImageThumbnail={data.account.profile_image_thumbnail}>
	{#if isSaved}
		<Button href="/profile" size="sm" variant="ghost">Return to profile</Button>
	{:else if isSubmitting}
		<Button disabled variant="ghost" type="button">
			<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
			Saving...
		</Button>
	{:else}
		<Button href="/profile" size="sm" variant="ghost">Cancel</Button>
		<Button href="/profile" size="sm">Save changes</Button>
	{/if}
</AccountBanner>

<div class="py-6 sm:flex sm:gap-x-16">
	<aside class="overflow-hidden rounded-md border sm:w-48 sm:border-none md:w-64">
		<Sidebar />
	</aside>
	<div class="flex-1 space-y-12 pt-4 sm:pt-0">
		<div>
			<AccountFormSection title="Email and password" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="email-verification">Email verification</Label>
						<div class="text-xs text-muted">Your email has been verified</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end gap-x-4">
                        <div>
                            <Badge variant="secondary">Not verified</Badge>
                        </div>
                        <div>
                            <Button variant="ghost" size="sm">Resend verification email</Button>
                        </div>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="change-email">Change email</Label>
						<div class="text-xs text-muted">
                            Change your email address, you will be required to reverify your email
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<Button variant="ghost" size="sm">Change email</Button>
					</div>
				</FieldContainerX>

				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="change-password">Change password</Label>
						<div class="text-xs text-muted">
							Change your accounts password
						</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
                        <Button variant="ghost" size="sm">Change password</Button>
					</div>
				</FieldContainerX>
			</div>
		</div>

		<div>
			<AccountFormSection title="Danger zone" />
			<div class="mt-4 space-y-4 divide-y divide-gray-100 border-t border-gray-200 text-sm">
				<FieldContainerX>
					<div class="col-span-12 flex-row items-center md:col-span-6">
						<Label for="delete-account">Delete account</Label>
						<div class="text-xs text-muted">Once you delete your account it cannot be undone</div>
					</div>
					<div class="col-span-12 flex items-center md:col-span-6 md:justify-end">
						<DeleteAccountDialog />
					</div>
				</FieldContainerX>
			</div>
		</div>
	</div>
</div>
