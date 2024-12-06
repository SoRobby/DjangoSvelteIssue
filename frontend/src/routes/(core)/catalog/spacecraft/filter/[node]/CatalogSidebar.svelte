<script lang="ts">
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select';

	// Original list of countries
	const countries = [
		{ name: 'United States', slug: 'united-states' },
		{ name: 'Canada', slug: 'canada' },
		{ name: 'Mexico', slug: 'mexico' },
		{ name: 'United Kingdom', slug: 'united-kingdom' },
		{ name: 'Germany', slug: 'germany' },
		{ name: "People's Republic of China", slug: 'china' }
	];

	const specialization = [
		{ name: 'ADCS Subsystem', slug: 'adcs-subsystem' },
		{ name: 'CDH Subsystem', slug: 'cdh-subsystem' },
		{ name: 'Mechanical Subsystem', slug: 'mechanical-subsystem' },
		{ name: 'Power Subsystem', slug: 'power-subsystem' },
		{ name: 'Propulsion Subsystem', slug: 'propulsion-subsystem' },
		{ name: 'Telecom Subsystem', slug: 'telecom-subsystem' },
		{ name: 'Thermal Subsystem', slug: 'thermal-subsystem' }
	];

	let countrySearch = $state('');
	let filteredCountries = $derived(filterItems(countries, countrySearch));
	let specializationSearch = $state('');
	let filteredSpecialization = $derived(filterItems(specialization, specializationSearch));

	function filterItems<T extends { name: string }>(list: T[], searchTerm: string) {
		return list.filter((item) => item.name.toLowerCase().includes(searchTerm.toLowerCase()));
	}
</script>

<div class="space-y-2 divide-y py-6 pr-4">
	<div class="flex items-end justify-between">
		<p class="text-lg font-medium text-primary">Filters</p>
		<p class="text-sm font-medium text-brand">Reset filter</p>
	</div>

	<!-- Filters below -->
	<div class="divide-y pl-1">
		todo...
	</div>
</div>
