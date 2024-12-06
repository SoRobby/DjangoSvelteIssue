<script lang="ts">
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';

	let { supplier, children } = $props();
</script>

<div class="pb-4 sm:pb-6">
	<div class="flex gap-4">
		<div class="w-24">
			<AspectRatio ratio={1 / 1} class="rounded-md bg-muted">
				<img
					src="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png"
					alt="#"
					class="rounded-md object-cover"
				/>
			</AspectRatio>
		</div>
		<div class="flex w-full">
			<div class="flex-1 space-y-1.5">
				<h1 class="text-2xl font-medium">{supplier.name}</h1>
				<p class="text-muted-foreground">{supplier.tagline}</p>
			</div>
			<div class="flex justify-end space-x-4">
				<Button variant="ghost" size="sm" href="/suppliers/{supplier.slug}">Return to profile</Button>
			</div>
		</div>
	</div>
</div>

<Separator />
