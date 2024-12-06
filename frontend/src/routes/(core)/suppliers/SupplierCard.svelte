<script lang="ts">
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import { Badge } from '$lib/components/ui/badge';
	import { Link } from '$lib/components/ui/link';

	let { supplier } = $props();
</script>

<div class="rounded-md border border-transparent p-2 hover:border-gray-100 relative">
	<AspectRatio ratio={3 / 2} class="rounded-md">
		<img
			src="https://via.placeholder.com/1080x720/eee?text=3:2"
			alt="Gray by Drew Beamer"
			class="w-full rounded-md object-cover"
		/>
	</AspectRatio>
    <a href="/suppliers/{supplier.slug}" class="absolute inset-0 block" aria-hidden="true">
        <span aria-hidden="true"></span>
    </a>
	<div class="mt-2 space-y-2">
		<div>
			<Badge variant="secondary" shape="square">Deep Space</Badge>
			<Badge variant="secondary" shape="square">SmallSat</Badge>
		</div>
		<h2 class="font-medium text-primary">{supplier.name}</h2>
		<p class="text-tertiary text-sm">
			{supplier.tagline}
		</p>
		<div>
			<Link href="/" class="text-sm">View profile</Link>
		</div>
	</div>
</div>
