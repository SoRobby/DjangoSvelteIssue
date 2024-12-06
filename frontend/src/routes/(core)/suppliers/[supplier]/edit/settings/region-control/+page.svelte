<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import * as Alert from '$lib/components/ui/alert';
	import { Info} from 'lucide-svelte';
    import AddCountryRestriction from './AddCountryRestriction.svelte';
	import RestrictedCountryCard from './RestrictedCountryCard.svelte';

	let { data } = $props();
	console.log(data);
</script>

<div class="space-y-12">
	<section class="space-y-6">
		<div class="border-b pb-4">
			<SupplierFormSection
				title="Region Control"
				description="Manage product visibility and sales restrictions by region"
			/>
		</div>

		<div>
			<Alert.Root class="border-blue-200 bg-blue-50 text-sm">
				<Info class="h-4 w-4 text-blue-400" />
				<Alert.Title class="text-blue-800">About Region Control</Alert.Title>
				<Alert.Description class="text-blue-700">
					Products will only be restricted for users who are verified to be residing in blocked
					countries. Verification is based on user profile information and compliance checks.</Alert.Description
				>
			</Alert.Root>
		</div>

		<div class="space-y-3">
			<div class="flex items-center justify-between">
				<div>
					<h3 class="font-semibold text-primary">Blocked Regions</h3>
					<p class="text-sm leading-6 text-muted">Countries where your products are restricted</p>
				</div>
				<div>
                    <AddCountryRestriction countries={data.countries} />
				</div>
			</div>

			<div class="rounded-md border p-4">
				<div class="text-sm font-medium text-muted">
					No countries/regions are currently restricted.
				</div>
			</div>

			<RestrictedCountryCard name="Iran" />
			<RestrictedCountryCard name="North Korea" />

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
