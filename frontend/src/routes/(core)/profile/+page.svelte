<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar';
	import { Button } from '$lib/components/ui/button';
	import { MapPin } from 'lucide-svelte';

	let { data } = $props();
</script>

<div class="flex items-center py-4 sm:py-6">
	<div class="flex flex-1 items-center space-x-4">
		<Avatar.Root class="h-12 w-12">
			<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
			<Avatar.Fallback>CN</Avatar.Fallback>
		</Avatar.Root>
		<div>
			<h1 class="text-2xl font-semibold text-primary">{data.user.first_name} {data.user.last_name}</h1>
			<p class="text-sm font-medium text-muted">@{data.user.username}</p>
		</div>
	</div>
	<div class="space-x-4">
		<Button size="sm" href="/settings/general">Edit</Button>
	</div>
</div>

<div class="py-16">
	<div
		class="mx-auto grid grid-cols-1 grid-rows-1 items-start gap-x-8 gap-y-8 md:grid-cols-3 lg:mx-0 lg:max-w-none"
	>
		<!-- Overview -->
		<div class="md:row-end-1 lg:col-start-3">
			<h2 class="sr-only">Summary</h2>
			<div class="rounded-lg bg-gray-50 shadow-sm ring-1 ring-gray-900/5">
				<dl class="flex flex-wrap py-6">
					<div class="flex-auto pl-6">
						<dt class="text-sm font-semibold leading-6 text-primary">User</dt>
						<dd class="mt-1 text-base font-semibold leading-6 text-primary">@{data.user.username}</dd>
					</div>

					<div class="flex-none self-end px-6 pt-4">
						<dt class="sr-only">Status</dt>
						<dd
							class="rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-600 ring-1 ring-inset ring-green-600/20"
						>
							Verified (FIX)
						</dd>
					</div>

					<div class="mt-6 w-full items-center space-y-4 border-t border-gray-900/5 px-6 pt-6">
						<div class="flex w-full flex-none items-center gap-x-4">
							<dt class="flex-none">
								<span class="sr-only">Client</span>
								<svg
									class="h-6 w-5 text-gray-400"
									viewBox="0 0 20 20"
									fill="currentColor"
									aria-hidden="true"
								>
									<path
										fill-rule="evenodd"
										d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-5.5-2.5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zM10 12a5.99 5.99 0 00-4.793 2.39A6.483 6.483 0 0010 16.5a6.483 6.483 0 004.793-2.11A5.99 5.99 0 0010 12z"
										clip-rule="evenodd"
									></path>
								</svg>
							</dt>
							<dd class="text-sm font-medium leading-6 text-primary">FirstName LastName</dd>
						</div>

						<div class="flex w-full flex-none items-center gap-x-4">
							<dt class="flex-none">
								<span class="sr-only">Country</span>
								<MapPin size="20" class="text-gray-400" />
							</dt>
							<dd class="text-sm font-medium leading-6 text-muted">CountryName</dd>
						</div>

						<div class="flex w-full flex-none items-center gap-x-4">
							<dt class="flex-none">
								<span class="sr-only">Date joined</span>
								<svg
									class="h-6 w-5 text-gray-400"
									viewBox="0 0 20 20"
									fill="currentColor"
									aria-hidden="true"
								>
									<path
										d="M5.25 12a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H6a.75.75 0 01-.75-.75V12zM6 13.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V14a.75.75 0 00-.75-.75H6zM7.25 12a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H8a.75.75 0 01-.75-.75V12zM8 13.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V14a.75.75 0 00-.75-.75H8zM9.25 10a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H10a.75.75 0 01-.75-.75V10zM10 11.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V12a.75.75 0 00-.75-.75H10zM9.25 14a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H10a.75.75 0 01-.75-.75V14zM12 9.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V10a.75.75 0 00-.75-.75H12zM11.25 12a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H12a.75.75 0 01-.75-.75V12zM12 13.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V14a.75.75 0 00-.75-.75H12zM13.25 10a.75.75 0 01.75-.75h.01a.75.75 0 01.75.75v.01a.75.75 0 01-.75.75H14a.75.75 0 01-.75-.75V10zM14 11.25a.75.75 0 00-.75.75v.01c0 .414.336.75.75.75h.01a.75.75 0 00.75-.75V12a.75.75 0 00-.75-.75H14z"
									></path>
									<path
										fill-rule="evenodd"
										d="M5.75 2a.75.75 0 01.75.75V4h7V2.75a.75.75 0 011.5 0V4h.25A2.75 2.75 0 0118 6.75v8.5A2.75 2.75 0 0115.25 18H4.75A2.75 2.75 0 012 15.25v-8.5A2.75 2.75 0 014.75 4H5V2.75A.75.75 0 015.75 2zm-1 5.5c-.69 0-1.25.56-1.25 1.25v6.5c0 .69.56 1.25 1.25 1.25h10.5c.69 0 1.25-.56 1.25-1.25v-6.5c0-.69-.56-1.25-1.25-1.25H4.75z"
										clip-rule="evenodd"
									></path>
								</svg>
							</dt>
							<dd class="text-sm font-medium leading-6 text-muted">CountryName</dd>
						</div>
					</div>
				</dl>
			</div>
		</div>

		<!-- About -->
		<div
			class="rounded-lg px-4 py-4 shadow-sm ring-1 ring-gray-900/5 sm:px-8 md:col-span-2 lg:row-span-2 lg:row-end-2"
		>
			<dl class="text-sm leading-6">
				<div class="sm:pr-4">
					<dt class="font-semibold text-primary">About</dt>
					<dd class="mt-2 text-muted">
						{data.user.bio}
					</dd>
				</div>
			</dl>
		</div>
	</div>
</div>
