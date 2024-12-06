<script lang="ts">
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import * as Dialog from '$lib/components/ui/dialog';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import * as Select from '$lib/components/ui/select';

	import Check from 'lucide-svelte/icons/check';
	import ChevronsUpDown from 'lucide-svelte/icons/chevrons-up-down';
	import { tick } from 'svelte';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import { cn } from '$lib/utils.js';

	let { countries } = $props();

	let open = $state(false);
	let slug = $state('');
	let triggerRef = $state<HTMLButtonElement>(null!);

	const selectedValue = $derived(countries.find((f: { slug: string }) => f.slug === slug)?.name);

	// We want to refocus the trigger button when the user selects
	// an item from the list so users can continue navigating the
	// rest of the form with the keyboard.
	function closeAndFocusTrigger() {
		open = false;
		tick().then(() => {
			triggerRef.focus();
		});
	}
</script>

<Dialog.Root>
	<Dialog.Trigger class={buttonVariants({ variant: 'outline', size: 'sm' })}
		>+ Add restriction</Dialog.Trigger
	>
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>Add country restriction</Dialog.Title>
			<Dialog.Description class="space-y-4 py-4">
				<p class="text-secondary">
					Select a country to restrict access to your company's product listings.
				</p>

				<Popover.Root bind:open>
					<Popover.Trigger bind:ref={triggerRef}>
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
					<Popover.Content id="country" class="w-[var(--bits-floating-anchor-width)] p-0">
						<Command.Root>
							<Command.Input placeholder="Search for a country..." />

							<Command.List>
								<Command.Empty>No countries found</Command.Empty>
								<Command.Group>
									{#each countries as country}
										<Command.Item
											value={country.slug}
											onSelect={() => {
												slug = country.slug;
												closeAndFocusTrigger();
											}}
										>
											<Check
												class={cn('mr-2 size-4', slug !== country.slug && 'text-transparent')}
											/>
											{country.name}
										</Command.Item>
									{/each}
								</Command.Group>
							</Command.List>
						</Command.Root>
					</Popover.Content>
				</Popover.Root>
			</Dialog.Description>
		</Dialog.Header>
		<Dialog.Footer class="flex gap-2">
			<Dialog.Close class={buttonVariants({ variant: 'ghost', size: 'sm' })}>Cancel</Dialog.Close>
			<Button size="sm" type="submit">Add restriction</Button>
		</Dialog.Footer>
	</Dialog.Content>
</Dialog.Root>
