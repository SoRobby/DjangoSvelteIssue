<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { X } from 'lucide-svelte';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';
	import * as Avatar from '$lib/components/ui/avatar';
</script>

<div class="flex justify-between rounded-md border p-4">
	<div class="flex items-center space-x-3">
		<Avatar.Root>
			<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
			<Avatar.Fallback>CN</Avatar.Fallback>
		</Avatar.Root>
		<div>
			<h4 class="font-medium leading-none text-primary">Sarah Johnson</h4>
			<div class="space-x-2">
				<span class="text-sm text-tertiary">sarah.j@company.com</span>
				<Badge variant="info">Admin</Badge>
			</div>
		</div>
	</div>
	<div>
		<AlertDialog.Root>
			<AlertDialog.Trigger>
				<Button size="icon" variant="ghost">
					<X size="20" class="text-muted hover:text-primary" />
				</Button>
			</AlertDialog.Trigger>
			<AlertDialog.Content>
				<AlertDialog.Header>
					<AlertDialog.Title>Remove user access</AlertDialog.Title>
					<AlertDialog.Description>
						Are you sure you want to remove XXXXX's access? They will no longer be able to manage
						the supplier profile.
					</AlertDialog.Description>
				</AlertDialog.Header>
				<AlertDialog.Footer>
					<AlertDialog.Cancel class={buttonVariants({ variant: 'outline', size: 'sm' })}>
						Cancel
					</AlertDialog.Cancel>
					<AlertDialog.Action class={buttonVariants({ variant: 'destructive', size: 'sm' })}>
						Remove access
					</AlertDialog.Action>
				</AlertDialog.Footer>
			</AlertDialog.Content>
		</AlertDialog.Root>
	</div>
</div>
