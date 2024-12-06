<script lang="ts">
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import * as Avatar from '$lib/components/ui/avatar';
	import * as HoverCard from '$lib/components/ui/hover-card';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { BadgeCheck, Box, FileText, MoreVertical } from 'lucide-svelte';
	import * as Tooltip from '$lib/components/ui/tooltip';

	let {
		itemName = 'Unknown name',
		itemSlug = 'unknown-slug',
		itemImage = '',
		itemDryMass = null,
		itemPowerConsumption = null,
		itemIsFlightProven = false,
		itemDatasheet = false,
		itemCad = false,
		supplierName = 'Unknown supplier',
		supplierLogo = '',
		supplierIsPremium = false,
		showMenu = false
	}: {
		itemName: string;
		itemSlug?: string;
		itemImage?: string;
		itemDryMass?: number | null;
		itemPowerConsumption?: number | null;
		itemIsFlightProven?: boolean;
		itemDatasheet?: boolean;
		itemCad?: boolean;
		supplierName?: string;
		supplierLogo?: string;
		supplierIsPremium?: boolean;
		showMenu?: boolean;
	} = $props();
</script>

<div class="overflow-hidden rounded-md border bg-slate-100 hover:border-gray-300">
	<div class="relative bg-white">
		<div class="relative">
			<AspectRatio ratio={3 / 2} class="rounded-md">
				<img
					src={itemImage}
					alt="Gray by Drew Beamer"
					class="h-full w-full rounded-t-md object-cover"
				/>
			</AspectRatio>
			<a href="/catalog/spacecraft/detail/{itemSlug}" class="absolute inset-0 block" aria-hidden="true">
				<span aria-hidden="true"></span>
			</a>
		</div>
		{#if showMenu}
			<div class="absolute right-2 top-2 z-20">
				<DropdownMenu.Root>
					<DropdownMenu.Trigger class={buttonVariants({ variant: 'ghost', size: 'icon' })}>
						<MoreVertical class="h-4 w-4" />
					</DropdownMenu.Trigger>
					<DropdownMenu.Content align="end" preventScroll={false}>
						<DropdownMenu.Group>
							<DropdownMenu.Item>Compare</DropdownMenu.Item>
							<DropdownMenu.Item>Favorite</DropdownMenu.Item>
							<DropdownMenu.Item>View datasheet</DropdownMenu.Item>
							<DropdownMenu.Separator />
							<DropdownMenu.Item>Edit</DropdownMenu.Item>
						</DropdownMenu.Group>
					</DropdownMenu.Content>
				</DropdownMenu.Root>
			</div>
		{/if}
		{#if itemIsFlightProven}
			<div class="absolute left-2 top-2">
				<Tooltip.Provider>
					<Tooltip.Root>
						<Tooltip.Trigger class="cursor-default">
							<Badge variant="secondary">Flight proven</Badge>
						</Tooltip.Trigger>
						<Tooltip.Content class="w-48">
							<p>
								<span class="font-medium">Flight proven</span> means the product been successfully demonstrated
								in space.
							</p>
						</Tooltip.Content>
					</Tooltip.Root>
				</Tooltip.Provider>
			</div>
		{/if}
	</div>

	<div class="relative px-3 pt-3">
		<h2 class="font-medium">{itemName}</h2>
		<a href="/catalog/spacecraft/detail/{itemSlug}" class="absolute inset-0 z-10 block" aria-hidden="true"> </a>
	</div>

	<div class="relative flex px-1 pt-2">
		<div
			class="relative z-20 flex shrink items-center gap-x-2 px-2 text-sm font-medium hover:underline"
		>
			<Avatar.Root class="h-7 w-7 border">
				<Avatar.Image src={supplierLogo} />
				<Avatar.Fallback>
					{supplierName[0].toUpperCase()}{supplierName[1].toUpperCase()}
				</Avatar.Fallback>
			</Avatar.Root>
			{supplierName}
			{#if supplierIsPremium}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="size-5 text-brand"
				>
					<path
						fill-rule="evenodd"
						d="M16.403 12.652a3 3 0 0 0 0-5.304 3 3 0 0 0-3.75-3.751 3 3 0 0 0-5.305 0 3 3 0 0 0-3.751 3.75 3 3 0 0 0 0 5.305 3 3 0 0 0 3.75 3.751 3 3 0 0 0 5.305 0 3 3 0 0 0 3.751-3.75Zm-2.546-4.46a.75.75 0 0 0-1.214-.883l-3.483 4.79-1.88-1.88a.75.75 0 1 0-1.06 1.061l2.5 2.5a.75.75 0 0 0 1.137-.089l4-5.5Z"
						clip-rule="evenodd"
					/>
				</svg>
			{/if}
			<a href="/suppliers/profile" class="absolute inset-0 z-10 block" aria-hidden="true">
				<span aria-hidden="true"></span>
			</a>
		</div>
		<a href="/catalog/spacecraft/detail/{itemSlug}" class="absolute inset-0 z-10 block" aria-hidden="true">
			<span aria-hidden="true"></span>
		</a>
	</div>
	<div class="text-muted-foreground relative px-3 pb-3 text-xs font-medium">
		<a href="/catalog/spacecraft/detail/{itemSlug}" class="absolute inset-0 z-10 block" aria-hidden="true">
			<span aria-hidden="true"></span>
		</a>
		<div class="flex items-center justify-between">
			{#if itemDryMass || itemPowerConsumption}
				<div class="flex gap-x-2 divide-x divide-gray-300 pt-2 text-tertiary">
					{#if itemDryMass && itemPowerConsumption}
						<div>Mass: {itemDryMass} kg</div>
						<div class="pl-2">Power: {itemPowerConsumption} W</div>
					{:else}
						{#if itemDryMass}
							<div>Mass: {itemDryMass} kg</div>
						{/if}
						{#if itemPowerConsumption}
							<div>Power: {itemPowerConsumption} W</div>
						{/if}
					{/if}
				</div>
			{/if}
			{#if itemDatasheet || itemCad}
				<div class="flex gap-x-2 divide-x divide-gray-300 pt-2 text-tertiary">
					{#if itemDatasheet}
						<div class="z-30">
							<Tooltip.Provider>
								<Tooltip.Root>
									<Tooltip.Trigger><FileText class="h-4 w-4 cursor-default" /></Tooltip.Trigger>
									<Tooltip.Content class="w-40">
										<p class="font-normal">Datasheet available for download</p>
									</Tooltip.Content>
								</Tooltip.Root>
							</Tooltip.Provider>
						</div>
					{/if}
					{#if itemCad}
						<div class="pl-2 z-30">
							<Tooltip.Provider>
								<Tooltip.Root>
									<Tooltip.Trigger><Box class="h-4 w-4 cursor-default" /></Tooltip.Trigger>
									<Tooltip.Content class="w-40">
										<p class="font-normal">CAD file available for download</p>
									</Tooltip.Content>
								</Tooltip.Root>
							</Tooltip.Provider>
						</div>
					{/if}
				</div>
			{/if}
		</div>
	</div>
</div>
