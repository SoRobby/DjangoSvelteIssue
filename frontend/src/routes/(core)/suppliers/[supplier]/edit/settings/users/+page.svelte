<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import * as Alert from '$lib/components/ui/alert';
	import { Info, User } from 'lucide-svelte';
	import UserCard from './UserCard.svelte';
	import AddNewUser from './AddNewUser.svelte';
</script>

<div class="space-y-12">
	<section class="space-y-6">
		<div class="border-b pb-4">
			<SupplierFormSection
				title="User Management"
				description="Manage team members who can access your supplier profile"
			/>
		</div>

		<div>
			<Alert.Root class="border-blue-200 bg-blue-50 text-sm">
				<Info class="h-4 w-4 text-blue-400" />
				<Alert.Title class="text-blue-800">About User Management</Alert.Title>
				<Alert.Description class="text-blue-700">
					All users added to your supplier profile will have full administrative access to manage
					company information, products, and other users.</Alert.Description
				>
			</Alert.Root>
		</div>

		<div class="space-y-3">
			<div class="flex items-center justify-between">
				<div>
					<h3 class="font-semibold text-primary">Team Members</h3>
					<p class="text-sm leading-6 text-muted">Users who can manage your supplier profile</p>
				</div>
				<div>
					<AddNewUser />
				</div>
			</div>

			<div class="rounded-md border py-8 text-center text-muted">
				<User size="36" class="mx-auto mb-2 opacity-50" />
				<p>No users who can manage supplier profile</p>
			</div>

			<UserCard />
			<UserCard />
			<UserCard />
		</div>

		<div>
			<Alert.Root class="border-gray-200 bg-gray-50 text-sm">
				<Alert.Title class="text-tertiary">Need Assistance?</Alert.Title>
				<Alert.Description class="text-muted">
					If you're unsure about which countries to restrict or have questions about export
					controls, please consult your company's legal team or compliance department or reach out
					to our support team for assistance.
				</Alert.Description>
			</Alert.Root>
		</div>
	</section>
</div>
