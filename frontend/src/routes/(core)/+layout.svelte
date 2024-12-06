<script lang="ts">
	import { Header } from '$lib/components/layout/header';
	import { Main } from '$lib/components/layout/main';

	let { data, children } = $props();
</script>

<Header userData={data.user} />
<Main variant="default" container="default">
	{@render children()}
</Main>
