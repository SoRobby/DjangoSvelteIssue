<script lang="ts">
	import type { SubmitFunction } from './$types';
	import { enhance } from '$app/forms';
	import { Button } from '$lib/components/ui/button';
	import { Label } from '$lib/components/ui/label';
	import { FieldContainer } from '$lib/components/layout/field-container';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { LoaderCircle } from 'lucide-svelte';
	import Check from 'lucide-svelte/icons/check';
	import ChevronsUpDown from 'lucide-svelte/icons/chevrons-up-down';
	import { tick } from 'svelte';
	import * as Alert from '$lib/components/ui/alert';
	import * as Command from '$lib/components/ui/command';
	import * as Popover from '$lib/components/ui/popover';
	import { cn } from '$lib/utils.js';

	let { name, email, organization, selectedCountrySlug, countries } = $props();

	// Form state
	let isSubmitting = $state(false);
	let isSubmitted = $state(false);

	let formName = $state(name);
	let formEmail = $state(email);
	let formOrganization = $state(organization);

	let formRequestDatasheet = $state(false);
	let formRequestIcd = $state(false);
	let formRequestOptionsSheet = $state(false);
	let formRequestUserManual = $state(false);
	let formRequestCadModel = $state(false);
	let formRequestQuotation = $state(false);
	let formRequestLeadTime = $state(false);
	let formRequestHeritage = $state(false);

	// Country select state
	let open = $state(false);
	let slug = $state(selectedCountrySlug);
	let triggerRef = $state<HTMLButtonElement>(null!);

	const selectedValue = $derived(countries.find((f: { slug: string }) => f.slug === slug)?.name);

	function closeAndFocusTrigger() {
		open = false;
		tick().then(() => {
			triggerRef.focus();
		});
	}

	// Form submission handler
	const handleSubmit: SubmitFunction = ({ formData }) => {
		isSubmitting = true;

		formData.append('country', slug?.toString() || '');

		return async ({ result, update }) => {
			// Do something after the form is submitted (e.g. hide a loader or show a success message)
			isSubmitting = false;
			isSubmitted = true;
			await update();

			// Reset the form to its initial state
			formName = name;
			formEmail = email;
			formOrganization = organization;
			formRequestDatasheet = false;
			formRequestIcd = false;
			formRequestOptionsSheet = false;
			formRequestUserManual = false;
			formRequestCadModel = false;
			formRequestQuotation = false;
			formRequestLeadTime = false;
			formRequestHeritage = false;
		};
	};
</script>

<div id="request-information-form" class="space-y-3 rounded-md border bg-white px-6 py-5">
	<h3 class="font-medium">Request Information Form</h3>

	{#if isSubmitted}
		<Alert.Root class="bg-green-50 text-green-800">
			<Alert.Title>Inquiry message sent</Alert.Title>
			<Alert.Description>
				<div>
					Your inquiry message has been successfully sent to the supplier. Response time will vary
					depending on supplier, product, and information requested.
				</div>
				<div class="mt-4">
					Have another inquiry? <Button onclick={() => isSubmitted=false} variant="none" size="none" class="ml-2 underline">Send another inquiry</Button>
				</div>
			</Alert.Description>
		</Alert.Root>
	{:else}
		<form method="POST" action="?/submitItemInquiry" class="pt-4" use:enhance={handleSubmit}>
			<div class="grid grid-cols-6 gap-4 md:grid-cols-12 md:gap-x-8 md:gap-y-4">
				<FieldContainer class="col-span-6">
					<Label for="name">Name</Label>
					<Input type="text" id="name" name="name" bind:value={formName} required />
				</FieldContainer>

				<FieldContainer class="col-span-6">
					<Label for="email">Email</Label>
					<div>
						<Input type="email" id="email" name="email" bind:value={formEmail} required />
						<p class="text-tertiary mt-1 text-xs">
							It is recommended to use your organization email address and not generic email
							addresses such as Gmail, Yahoo, etc.
						</p>
					</div>
				</FieldContainer>

				<FieldContainer class="col-span-6">
					<Label for="organization">Organization</Label>
					<Input
						type="text"
						id="organization"
						name="organization"
						bind:value={formOrganization}
						required
					/>
				</FieldContainer>

				<FieldContainer class="col-span-6">
					<Label for="country">Country</Label>
					<!-- <Input type="text" id="country" name="country" value={countrySlug} required /> -->
					<Popover.Root bind:open>
						<Popover.Trigger bind:ref={triggerRef}>
							{#snippet child({ props })}
								<Button
									variant="outline"
									class="justify-between"
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
				</FieldContainer>
			</div>

			<FieldContainer class="pt-4">
				<Label for="content">Message</Label>
				<div>
					<Textarea id="content" name="content" required />
					<p class="text-tertiary mt-1 text-xs">
						Please be detailed in your message, including any specific requirements or questions you
						may have.
					</p>
				</div>
			</FieldContainer>

			<div class="pt-4">
				<p class="text-sm font-medium">Request Options</p>
				<div class="grid grid-cols-2 gap-4 pt-2">
					<div class="space-y-2">
						<div class="flex items-center gap-2">
							<Checkbox
								id="request-datasheet"
								name="request-datasheet"
								bind:checked={formRequestDatasheet}
							/>
							<Label
								for="request-datasheet"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Datasheet
							</Label>
						</div>

						<div class="flex items-center gap-2">
							<Checkbox id="request-icd" name="request-icd" bind:checked={formRequestIcd} />
							<Label
								for="request-icd"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Interface Control Document (ICD)
							</Label>
						</div>

						<div class="flex items-center gap-2">
							<Checkbox
								id="request-options-sheet"
								name="request-options-sheet"
								bind:checked={formRequestOptionsSheet}
							/>
							<Label
								for="request-options-sheet"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Options sheet
							</Label>
						</div>

						<div class="flex items-center gap-2">
							<Checkbox
								id="request-user-manual"
								name="request-user-manual"
								bind:checked={formRequestUserManual}
							/>
							<Label
								for="request-user-manual"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								User manual
							</Label>
						</div>
					</div>

					<div class="space-y-2">
						<div class="flex items-center gap-2">
							<Checkbox
								id="request-cad-model"
								name="request-cad-model"
								bind:checked={formRequestCadModel}
							/>
							<Label
								for="request-cad-model"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								CAD model
							</Label>
						</div>

						<div class="flex items-center gap-2">
							<Checkbox
								id="request-quotation"
								name="request-quotation"
								bind:checked={formRequestQuotation}
							/>
							<Label
								for="request-quotation"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Quotation
							</Label>
						</div>

						<div class="flex items-center gap-2">
							<Checkbox
								id="request-lead-time"
								name="request-lead-time"
								bind:checked={formRequestLeadTime}
							/>
							<Label
								for="request-lead-time"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Lead time
							</Label>
						</div>

						<div class="group flex items-center gap-2">
							<Checkbox
								id="request-heritage"
								name="request-heritage"
								bind:checked={formRequestHeritage}
							/>
							<Label
								for="request-heritage"
								class="cursor-pointer text-sm font-normal leading-none text-gray-600"
							>
								Flight proven / heritage information
							</Label>
						</div>
					</div>
				</div>
			</div>

			<div class="flex justify-end pt-8">
				{#if isSubmitting}
					<Button disabled variant="ghost" type="button" size="sm">
						<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
						Sending request...
					</Button>
				{:else}
					<Button type="submit" size="sm">Submit request</Button>
				{/if}
			</div>
		</form>
	{/if}
</div>
