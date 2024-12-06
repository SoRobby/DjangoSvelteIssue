<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { Globe, X, Shield } from 'lucide-svelte';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';

	let { name }: { name: string } = $props();
</script>

<div class="flex items-center justify-between rounded-md border bg-gray-50 px-3 py-2">
	<div class="flex items-center space-x-3">
		<Globe class="h-5 w-5 text-tertiary" />
		<span class="font-medium">{name}</span>
	</div>
	<div class="flex items-center space-x-3">
		<Badge variant="outline" shape="square" class="gap-x-2">
			<Shield size="14" />
			Restricted</Badge
		>

		<AlertDialog.Root>
			<AlertDialog.Trigger>
				<Button size="icon" variant="ghost">
					<X size="20" class="text-muted hover:text-primary" />
				</Button>
			</AlertDialog.Trigger>
			<AlertDialog.Content>
				<AlertDialog.Header>
					<AlertDialog.Title>Remove restriction</AlertDialog.Title>
					<AlertDialog.Description>
						Are you sure you want to remove the restriction for XXXX? Your products will become
						visible in this country.
					</AlertDialog.Description>
				</AlertDialog.Header>
				<AlertDialog.Footer>
					<AlertDialog.Cancel class={buttonVariants({ variant: 'ghost', size: 'sm' })}>
						Cancel
					</AlertDialog.Cancel>
					<AlertDialog.Action class={buttonVariants({ variant: 'destructive', size: 'sm' })}>
						Remove restriction
					</AlertDialog.Action>
				</AlertDialog.Footer>
			</AlertDialog.Content>
		</AlertDialog.Root>
	</div>
</div>
