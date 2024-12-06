<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';
	import { EllipsisVertical, MapPin } from 'lucide-svelte';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';

	let { isHeadquarters }: { isHeadquarters: boolean } = $props();
</script>

<div class="space-y-2 rounded-md border px-4 py-2">
	<div class="flex justify-between">
		<div class="flex items-center space-x-2">
			<MapPin size="18" class="text-tertiary" />
			<h3 class="font-medium text-primary">Global Headquarters</h3>
			{#if isHeadquarters}
				<Badge variant="secondary">HQ</Badge>
			{/if}
		</div>
		<div>
			<DropdownMenu.Root>
				<DropdownMenu.Trigger>
					<Button variant="ghost" size="none" class="rounded-full px-1 py-1 text-muted">
						<span class="sr-only">Tooltip for xxxxx</span>
						<EllipsisVertical class="h-5 w-5" />
					</Button>
				</DropdownMenu.Trigger>
				<DropdownMenu.Content preventScroll={false} align="end">
					<DropdownMenu.Group>
						<DropdownMenu.Item>Edit location</DropdownMenu.Item>
						{#if !isHeadquarters}
							<DropdownMenu.Item>Set as HQ</DropdownMenu.Item>
						{/if}
						<DropdownMenu.Item>Delete location</DropdownMenu.Item>
					</DropdownMenu.Group>
				</DropdownMenu.Content>
			</DropdownMenu.Root>
		</div>
	</div>

	<div class="text-sm text-tertiary">
		<p>1234 Main St, Suite 100</p>
		<p>City, State, Zip</p>
		<p>Country</p>
	</div>
</div>
