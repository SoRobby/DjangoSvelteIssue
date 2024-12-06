<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar';
	import { AspectRatio } from '$lib/components/ui/aspect-ratio';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import { copyLinkToClipboard } from '$lib/utils/copyLinkToClipboard';

	let { supplier } = $props();
</script>

<div class="pb-4 sm:pb-6">
	<div class="flex gap-4">
		<div class="w-24">
			<AspectRatio ratio={1 / 1} class="bg-muted rounded-md">
				<img
					src="https://developers.elementor.com/docs/assets/img/elementor-placeholder-image.png"
					alt="#"
					class="rounded-md object-cover"
				/>
			</AspectRatio>
		</div>
		<div class="flex w-full">
			<div class="flex-1 space-y-1.5">
				<h1 class="flex items-center gap-x-2 text-2xl font-medium">
					{supplier.name}
					{#if supplier.is_premium}
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 20 20"
							fill="currentColor"
							class="text-brand mt-1 size-6"
						>
							<path
								fill-rule="evenodd"
								d="M16.403 12.652a3 3 0 0 0 0-5.304 3 3 0 0 0-3.75-3.751 3 3 0 0 0-5.305 0 3 3 0 0 0-3.751 3.75 3 3 0 0 0 0 5.305 3 3 0 0 0 3.75 3.751 3 3 0 0 0 5.305 0 3 3 0 0 0 3.751-3.75Zm-2.546-4.46a.75.75 0 0 0-1.214-.883l-3.483 4.79-1.88-1.88a.75.75 0 1 0-1.06 1.061l2.5 2.5a.75.75 0 0 0 1.137-.089l4-5.5Z"
								clip-rule="evenodd"
							/>
						</svg>
					{/if}
				</h1>
				<p class="text-muted-foreground">{supplier.tagline}</p>
			</div>
			<div class="flex justify-end space-x-4">
				<Button variant="outline" size="sm" href="/suppliers/{supplier.slug}/edit">Edit profile</Button>
			</div>
		</div>
	</div>
</div>

<Separator />
