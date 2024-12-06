<script>
	let { children } = $props();
	import { Header } from '$lib/components/layout/header';
	import { Main } from '$lib/components/layout/main';
	import { Footer } from '$lib/components/layout/footer';
</script>

<Main variant="default">
	{@render children()}
</Main>
<Footer />
