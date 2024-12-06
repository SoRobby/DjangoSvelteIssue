<script lang="ts">
	import { Main } from '$lib/components/layout/main';
	import { Link } from '$lib/components/ui/link';
	import { Header } from '$lib/components/layout/header';
	import { PUBLIC_API_ROOT_URL, PUBLIC_SITE_NAME } from '$env/static/public';
	import { JsonCard } from '$lib/components/dev/json-card';
	import ExampleGif from '$lib/assets/example.gif';

	let { data } = $props();
</script>

<Header userData={data.user} />

<Main variant="secondary" container="default">
	<div class="rounded-md border border-red-200 bg-red-50 p-4 pb-4 sm:pb-6">
		<h1 class="text-2xl font-bold text-red-600">ISSUE</h1>
		<div class="font-medium text-red-700 space-y-2">
			<p>
				Anytime I make changes to a typescript-related file (e.g., +page.server.ts,
				+layout.server.ts, hooks.server.ts, etc...) the browser takes 4-10 seconds to refresh. It
				just depends on the change; I have noticed as the project gets larger refresh times are
				starting to take longer and longer...
			</p>
			<p>When updating Svelte files +layout.svelte or +page.svelte the change is instantaneous.</p>
			<p>Admin account is email = admin@admin.com | pw = admin</p>
		</div>

		<div class="mt-2">
			<img src={ExampleGif} alt="Example gif" class="h-auto w-full" />
		</div>
	</div>

	<div class="mt-4 grid grid-cols-1 gap-4 rounded-md border p-4 sm:grid-cols-3">
		<div>
			<h2 class="border-b pb-1 text-lg font-medium">Main</h2>
			<div class="mt-2 grid text-nowrap text-sm font-medium">
				<Link href="/profile" class="hover:underline">User profile</Link>
				<Link href="/settings/general" class="hover:underline">User settings</Link>
				<Link href="/catalog" class="hover:underline">Catalog</Link>
				<Link href="/catalog/satellite/item" class="hover:underline">Catalog products</Link>
				<Link href="/suppliers" class="hover:underline">Suppliers</Link>
				<Link href="/tools" class="hover:underline">Tools</Link>
				<Link href="/articles" class="hover:underline">Articles</Link>
			</div>
		</div>

		<div>
			<h2 class="border-b pb-1 text-lg font-medium">Authentication</h2>
			<div class="mt-2 grid text-nowrap text-sm font-medium">
				<Link href="/login" class="hover:underline">Login</Link>
				<Link href="/register" class="hover:underline">Register</Link>
				<Link href="/forgot-password" class="hover:underline">Forgot password</Link>
				<Link href="/reset-password" class="hover:underline">Reset password</Link>
				<Link href="/" class="hover:underline">Logout</Link>
			</div>
		</div>

		<div>
			<h2 class="border-b pb-1 text-lg font-medium">Development</h2>
			<div class="mt-2 grid text-nowrap text-sm font-medium">
				<Link href="/dev/api" class="hover:underline">API Endpoints</Link>
				<Link href="/dev/components" class="hover:underline">Components</Link>
				<Link href="/" class="hover:underline">Users</Link>
			</div>
		</div>

		<div class="col-span-1 border-t pt-4 sm:col-span-3">
			<div class="text-secondary text-sm">
				<span class="font-medium">PUBLIC_API_ROOT_URL:</span>
				{PUBLIC_API_ROOT_URL}
			</div>
			<div class="text-secondary text-sm">
				<span class="font-medium">PUBLIC_SITE_NAME:</span>
				{PUBLIC_SITE_NAME}
			</div>

			<JsonCard data={data.user} />
		</div>
	</div>
</Main>

{#snippet productCard(title: string, imagePath: string, href: string)}
	<a
		{href}
		class="text-primary group flex flex-col items-center gap-y-2 rounded-md border bg-zinc-100 p-3 text-center hover:border-blue-200 hover:bg-blue-50"
	>
		<img src={imagePath} alt="{title} category" class="h-16 w-16 rounded-md object-cover" />
		<h3 class="group-hover:text-brand group-hover:underline">{title}</h3>
	</a>
{/snippet}
