<script lang="ts">
	import '../app.css';
	import '../styles/custom.css';

	import type { Snippet } from 'svelte';
	import { onMount, setContext } from 'svelte';
	import { Toaster } from '$lib/components/ui/sonner';
	import { DevBar } from '$lib/components/dev/dev-bar';
	import { FeedbackModal } from '$lib/components/layout/feedback-modal';
	import authApi from '$lib/api/client/auth';
	import userState from '$lib/stores/userState';
	import { Header } from '$lib/components/layout/header';
	import { Footer } from '$lib/components/layout/footer';

	let { data, children }: { data: any; children: Snippet } = $props();

	onMount(() => {
		authApi.initRefreshTokenCycle();
		return () => {
			authApi.clearRefreshInterval();
		};
	});

	const user = userState({
		username: null,
		email: null
	});

	setContext('user', user);
</script>

<Toaster position="top-right" />
{@render children()}
<FeedbackModal email={data.user.email} />
<DevBar userData={data.user} />
<Footer />