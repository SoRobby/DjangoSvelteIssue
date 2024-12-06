<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { Button, buttonVariants } from '$lib/components/ui/button';
	import { FieldContainer } from '$lib/components/layout/field-container';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
</script>

<AlertDialog.Root>
	<AlertDialog.Trigger class={buttonVariants({ variant: 'ghost', size: 'sm' })}>
		<Button variant="ghost" size="sm">Delete account</Button>
	</AlertDialog.Trigger>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
			<AlertDialog.Description>
				<p>
					This action cannot be undone. This will permanently delete your account and remove your
					data from our servers.
				</p>
				<FieldContainer class="pt-4">
					<Label for="password">Password</Label>
					<Input
						type="password"
						id="password"
						name="password"
						autocomplete="off"
						required
					/>
				</FieldContainer>
			</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer class="pt-4">
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<AlertDialog.Action class={buttonVariants({ variant: 'destructive' })}
				>Delete</AlertDialog.Action
			>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
