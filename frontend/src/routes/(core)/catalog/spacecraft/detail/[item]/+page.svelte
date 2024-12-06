<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import { Label } from '$lib/components/ui/label';
	import * as Pagination from '$lib/components/ui/pagination';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { Input } from '$lib/components/ui/input';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import RequestInfoForm from './RequestInfoForm.svelte';
	import * as Avatar from '$lib/components/ui/avatar';
	import { smoothScrollTo } from '$lib/utils';
	import {
		ChevronDown,
		ChevronRight,
		Info,
		FileText,
		StickyNote,
		Download,
		ArrowRightFromLine
	} from 'lucide-svelte';

	import * as Tooltip from '$lib/components/ui/tooltip';
	import PropertiesTable from './PropertiesTable.svelte';
	import { JsonCard } from '$lib/components/dev/json-card';

	let { data } = $props();

	let fullName = $state('');
	if (data.user.first_name && data.user.last_name) {
		fullName = `${data.user.first_name} ${data.user.last_name}`;
	} else if (data.user.first_name) {
		fullName = data.user.first_name;
	}
</script>

<!-- Breadcrumb navigation -->
<div class="md:flex md:justify-between">
	<Breadcrumb.Root class="flex-1 pb-4 sm:pb-6">
		<Breadcrumb.List>
			<Breadcrumb.Item>
				<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
			</Breadcrumb.Item>
			<Breadcrumb.Separator>/</Breadcrumb.Separator>
			<Breadcrumb.Item>
				<Breadcrumb.Link href="/catalog">Catalog</Breadcrumb.Link>
			</Breadcrumb.Item>
			<Breadcrumb.Separator>/</Breadcrumb.Separator>
			<Breadcrumb.Item>
				<Breadcrumb.Link href="/catalog/spacecraft/filter">Spacecraft</Breadcrumb.Link>
			</Breadcrumb.Item>
			<Breadcrumb.Separator>/</Breadcrumb.Separator>
			<Breadcrumb.Item>
				<Breadcrumb.Link href="/catalog/spacecraft/filter/{data.item.node.slug}"
					>{data.item.node.name}</Breadcrumb.Link
				>
			</Breadcrumb.Item>
			<Breadcrumb.Separator>/</Breadcrumb.Separator>
			<Breadcrumb.Item>
				<Breadcrumb.Page>{data.item.name}</Breadcrumb.Page>
			</Breadcrumb.Item>
		</Breadcrumb.List>
	</Breadcrumb.Root>
	<div class="hidden md:block">
		<Button href="/suppliers/{data.item.supplier.slug}" size="sm" variant="outline"
			>Edit item</Button
		>
	</div>
</div>

<!-- Product -->
<div class="flex gap-8">
	<!-- left side -->
	<div class="flex-1">
		<AspectRatio ratio={3 / 2} class="bg-white">
			<img
				src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
				alt="Gray by Drew Beamer"
				class="h-full w-full rounded-md object-cover"
			/>
		</AspectRatio>

		<!-- Main content -->
		<div class="space-y-4 py-6">
			<div class="flex gap-8 rounded-md border bg-white px-6 py-2 font-medium">
				<div>
					<a
						href="#overview"
						class="text-tertiary hover:text-blue-600 hover:underline"
						onclick={(event) => {
							event.preventDefault();
							smoothScrollTo('overview');
						}}>Overview</a
					>
				</div>
				<div>
					<a
						href="#properties"
						class="text-tertiary hover:text-blue-600 hover:underline"
						onclick={(event) => {
							event.preventDefault();
							smoothScrollTo('properties');
						}}>Properties</a
					>
				</div>
				<div>
					<a
						href="#request-information-form"
						class="text-tertiary hover:text-blue-600 hover:underline"
						onclick={(event) => {
							event.preventDefault();
							smoothScrollTo('request-information-form');
						}}>Request Information Form</a
					>
				</div>
			</div>

			<!-- Overview -->
			<div id="overview" class="space-y-3 rounded-md border bg-white px-6 py-5">
				<h3 class="font-medium">Overview</h3>
				<p class="text-tertiary">
					{data.item.description}
				</p>
			</div>

			<!-- Properties -->
			<div id="properties" class="space-y-3 rounded-md border bg-white px-6 py-5">
				<h3 class="font-medium">Properties</h3>

				<PropertiesTable item={data.item} />
			</div>

			<!-- Inquiry -->
			<RequestInfoForm
				name={fullName}
				email={data.user?.email}
				organization={data.user?.organization}
				selectedCountrySlug={data.user?.country_slug}
				countries={data.countries}
			/>
		</div>
	</div>

	<!-- right sidebar -->
	<aside class="w-[416px] space-y-4">
		<!-- Main section -->

		<div class="space-y-10 rounded-md border bg-white px-6 py-5">
			<!-- main:overview -->
			<div class="space-y-5">
				<h1 class="text-2xl font-bold">{data.item.name}</h1>

				<div class="relative flex shrink items-center gap-x-2 text-sm font-medium hover:underline">
					<Avatar.Root class="border">
						<Avatar.Fallback>LM</Avatar.Fallback>
					</Avatar.Root>
					{data.item.supplier.name}
					{#if data.item.supplier.is_premium}
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 20 20"
							fill="currentColor"
							class="text-brand size-5"
						>
							<path
								fill-rule="evenodd"
								d="M16.403 12.652a3 3 0 0 0 0-5.304 3 3 0 0 0-3.75-3.751 3 3 0 0 0-5.305 0 3 3 0 0 0-3.751 3.75 3 3 0 0 0 0 5.305 3 3 0 0 0 3.75 3.751 3 3 0 0 0 5.305 0 3 3 0 0 0 3.751-3.75Zm-2.546-4.46a.75.75 0 0 0-1.214-.883l-3.483 4.79-1.88-1.88a.75.75 0 1 0-1.06 1.061l2.5 2.5a.75.75 0 0 0 1.137-.089l4-5.5Z"
								clip-rule="evenodd"
							/>
						</svg>
					{/if}
					<a href="/suppliers/{data.item.supplier.slug}" class="absolute inset-0 z-10 block" aria-hidden="true">
						<span aria-hidden="true"></span>
					</a>
				</div>
			</div>

			<!-- main:highlighted properties -->
			<div>
				<h2 class="font-medium">Highlighted Properties</h2>
				<div>
					<dl class="divide-y divide-gray-100">
						<div class="grid grid-cols-2 py-3">
							<dt class="text-muted text-sm font-medium">Category</dt>
							<dd class="text-sm">{data.item.taxonomy.name}</dd>
						</div>
					</dl>
					<div class="text-sm text-blue-600">
						<a
							href="#properties"
							onclick={(event) => {
								event.preventDefault();
								smoothScrollTo('properties');
							}}>View all properties</a
						>
					</div>
				</div>
			</div>
		</div>

		
	</aside>
</div>

<JsonCard {data} isExpanded={true} />
