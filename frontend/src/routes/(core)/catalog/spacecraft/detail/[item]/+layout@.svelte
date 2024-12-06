<script lang="ts">
	import { Header } from '$lib/components/layout/header';
	import { Main } from '$lib/components/layout/main';
	import { Footer } from '$lib/components/layout/footer';

	let { data, children } = $props();
</script>

<Header userData={data.user} />
<Main variant="secondary" container="default">
	{@render children()}
</Main>
<Footer />
