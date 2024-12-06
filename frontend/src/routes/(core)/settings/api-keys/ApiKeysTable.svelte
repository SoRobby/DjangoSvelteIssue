<script lang="ts">
	import * as Table from '$lib/components/ui/table';
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { X } from 'lucide-svelte';
	import { buttonVariants } from '$lib/components/ui/button';

	const ApiKeys = [
		{
			name: 'My First API',
			secret_key: 'sk-...pZ',
			date_created: '2021-10-01'
		},
		{
			name: 'Project Alpha API',
			secret_key: 'sk-...Rx',
			date_created: '2022-06-15'
		},
		{
			name: 'Development API',
			secret_key: 'sk-...MA',
			date_created: '2023-02-10'
		}
	];
</script>

<div class="overflow-hidden rounded-t-md">
	<Table.Root>
		<Table.Header class="rounded-md bg-slate-100">
			<Table.Row enableHoverBackground={false}>
				<Table.Head class="">Name</Table.Head>
				<Table.Head>Secret Key</Table.Head>
				<Table.Head>Date Created</Table.Head>
				<Table.Head>
					<span class="sr-only">Edit</span>
				</Table.Head>
			</Table.Row>
		</Table.Header>
		<Table.Body>
			{#each ApiKeys as ApiKey}
				<Table.Row enableHoverBackground={false}>
					<Table.Cell>{ApiKey.name}</Table.Cell>
					<Table.Cell>{ApiKey.secret_key}</Table.Cell>
					<Table.Cell>{ApiKey.date_created}</Table.Cell>
					<Table.Cell class="py-0 text-right">
						<AlertDialog.Root>
							<AlertDialog.Trigger class={buttonVariants({ variant: 'ghost', size: 'icon' })}>
								<X class="text-muted hover:text-primary" />
							</AlertDialog.Trigger>
							<AlertDialog.Content>
								<AlertDialog.Header>
									<AlertDialog.Title>Revoke secret key</AlertDialog.Title>
									<AlertDialog.Description>
										This API key will immediately be disabled. API requests made using this key will
										be rejected, which could cause any systems still depending on it to break.
									</AlertDialog.Description>
								</AlertDialog.Header>
								<AlertDialog.Footer>
									<AlertDialog.Cancel class={buttonVariants({ variant: 'outline', size: 'sm' })}>
										Cancel
									</AlertDialog.Cancel>
									<AlertDialog.Action
										class={buttonVariants({ variant: 'destructive', size: 'sm' })}
									>
										Revoke key
									</AlertDialog.Action>
								</AlertDialog.Footer>
							</AlertDialog.Content>
						</AlertDialog.Root>
					</Table.Cell>
				</Table.Row>
			{/each}
		</Table.Body>
	</Table.Root>
</div>
