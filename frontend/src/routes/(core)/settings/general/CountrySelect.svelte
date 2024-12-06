<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import Check from 'lucide-svelte/icons/check';
	import ChevronsUpDown from 'lucide-svelte/icons/chevrons-up-down';
	import { tick } from 'svelte';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import { cn } from '$lib/utils.js';

	// Props
	let { countries, selectedCountrySlug, onSelect } = $props();

	// Local state
	let open = $state(false);
	let slug = $state(selectedCountrySlug);
	let triggerRef = $state<HTMLButtonElement>(null!);

	const selectedValue = $derived(countries.find((f: { slug: string }) => f.slug === slug)?.name);

	// Focus back on the trigger button after selection
	function closeAndFocusTrigger() {
		open = false;
		tick().then(() => {
			triggerRef.focus();
		});
	}

	function selectCountry(countrySlug: string) {
		slug = countrySlug;
		onSelect?.(countrySlug); // Call the parent callback
		closeAndFocusTrigger();
	}
</script>

<Popover.Root bind:open>
	<Popover.Trigger bind:ref={triggerRef} id="country">
		{#snippet child({ props })}
			<Button
				variant="outline"
				class="w-full justify-between"
				{...props}
				role="combobox"
				aria-expanded={open}
			>
				{selectedValue || 'Select a country...'}
				<ChevronsUpDown class="ml-2 size-4 shrink-0 opacity-50" />
			</Button>
		{/snippet}
	</Popover.Trigger>
	<Popover.Content class="w-[var(--bits-floating-anchor-width)] p-0">
		<Command.Root>
			<Command.Input placeholder="Search for a country..." />

			<Command.List>
				<Command.Empty>No countries found</Command.Empty>
				<Command.Group>
					{#each countries as country}
						<Command.Item
							value={country.slug}
							onSelect={() => selectCountry(country.slug)}
						>
							<Check class={cn('mr-2 size-4', slug !== country.slug && 'text-transparent')} />
							{country.name}
						</Command.Item>
					{/each}
				</Command.Group>
			</Command.List>
		</Command.Root>
	</Popover.Content>
</Popover.Root>