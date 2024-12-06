<script lang="ts">
	import Sidebar from '../Sidebar.svelte';
	import AccountBanner from '../AccountBanner.svelte';
	import { Button } from '$lib/components/ui/button';
	import AccountFormSection from '../AccountFormSection.svelte';
	import CreateNewSecretKey from './CreateNewSecretKey.svelte';

	import ApiKeysTable from './ApiKeysTable.svelte';

	let { data } = $props();
</script>

<AccountBanner
	name={`${data.account.first_name} ${data.account.last_name}`}
	username={data.account.username}
	profileImageThumbnail={data.account.profile_image_thumbnail}
>
	<Button href="/profile" size="sm" variant="ghost">Return to profile</Button>
</AccountBanner>

<div class="py-6 sm:flex sm:gap-x-16">
	<aside class="overflow-hidden rounded-md border sm:w-48 sm:border-none md:w-64">
		<Sidebar />
	</aside>
	<div class="flex-1 space-y-12 pt-4 sm:pt-0">
		<div>
			<div class="flex items-center justify-between">
				<AccountFormSection title="API Keys" />
				<div>
					<CreateNewSecretKey />
				</div>
			</div>

			<div class="mt-4 space-y-4 border-t border-gray-200">
				<div class="text-muted mt-4 rounded-md border py-4 text-center text-sm">
					<p class="font-medium">You do not have any API keys</p>
				</div>

				<!-- API Table -->
				<ApiKeysTable />
			</div>
		</div>
	</div>
</div>
