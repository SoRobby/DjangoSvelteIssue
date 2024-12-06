<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';

	import * as Alert from '$lib/components/ui/alert';
	import { Badge } from '$lib/components/ui/badge';
	import { Button } from '$lib/components/ui/button';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import * as Command from '$lib/components/ui/command';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select';
	import { Switch } from '$lib/components/ui/switch';
</script>

<ComponentExample>
	<ComponentExample.Header>Text</ComponentExample.Header>
	<ComponentExample.Preview>
		<div class="grid grid-cols-8">
			<div>
				<div class="h-8 w-8 rounded-md bg-gray-900"></div>
				<div class="text-xs font-medium text-primary">Text primary</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-gray-800"></div>
				<div class="text-xs font-medium text-secondary">Text secondary</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-gray-600"></div>
				<div class="text-tertiary text-xs font-medium">Text tertiary</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-gray-500"></div>
				<div class="text-xs font-medium text-muted">Text muted</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-red-600"></div>
				<div class="text-error text-xs font-medium">Text error</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-yellow-600"></div>
				<div class="text-warning text-xs font-medium">Text warning</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-green-600"></div>
				<div class="text-success text-xs font-medium">Text success</div>
			</div>

			<div>
				<div class="h-8 w-8 rounded-md bg-blue-600"></div>
				<div class="text-info text-xs font-medium">Text info</div>
			</div>
		</div>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Borders</ComponentExample.Header>
	<ComponentExample.Preview>
		<div class="grid grid-cols-8">
			<div>
				<div class="h-8 w-8 rounded-md bg-gray-300"></div>
				<div class="text-xs font-medium text-link">

					<input class="px-2 py-1.5 border rounded-md bg-white">
				</div>
			</div>

		</div>
	</ComponentExample.Preview>
</ComponentExample>



<ComponentExample>
	<ComponentExample.Header>Alert</ComponentExample.Header>
	<ComponentExample.Preview>
		<Alert.Root variant="destructive">
			<Alert.Title>Error</Alert.Title>
			<Alert.Description>Your session has expired. Please login again.</Alert.Description>
		</Alert.Root>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Badge</ComponentExample.Header>
	<ComponentExample.Preview>
		<Badge variant="default">Badge</Badge>
		<Badge variant="secondary">Secondary</Badge>
		<Badge variant="accent">Accent</Badge>
		<Badge variant="outline">Outline</Badge>
		<Badge variant="success">Success</Badge>
		<Badge variant="warning">Warning</Badge>
		<Badge variant="destructive">Destructive</Badge>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Button</ComponentExample.Header>
	<ComponentExample.Preview>
		<div class="flex gap-4">
			<Button>Button</Button>
			<Button variant="secondary">Secondary</Button>
			<Button variant="outline">Outline</Button>
			<Button variant="destructive">Destructive</Button>
			<Button variant="ghost">Ghost</Button>
			<Button variant="link">Link</Button>
			<Button disabled>Please wait...</Button>
		</div>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Checkbox</ComponentExample.Header>
	<ComponentExample.Preview>
		<div class="items-top flex space-x-2">
			<Checkbox id="terms1" />
			<div class="grid gap-1.5 leading-none">
				<Label
					for="terms1"
					class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
				>
					Accept terms and conditions
				</Label>
				<p class="text-sm text-muted-foreground">
					You agree to our Terms of Service and Privacy Policy.
				</p>
			</div>
		</div>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Command</ComponentExample.Header>
	<ComponentExample.Preview>
		<Command.Root>
			<Command.Input placeholder="Type a command or search..." />
			<Command.List>
				<Command.Empty>No results found.</Command.Empty>
				<Command.Group heading="Suggestions">
					<Command.Item>Calendar</Command.Item>
					<Command.Item>Search Emoji</Command.Item>
					<Command.Item>Calculator</Command.Item>
				</Command.Group>
				<Command.Separator />
				<Command.Group heading="Settings">
					<Command.Item>Profile</Command.Item>
					<Command.Item>Billing</Command.Item>
					<Command.Item>Settings</Command.Item>
				</Command.Group>
			</Command.List>
		</Command.Root>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Input</ComponentExample.Header>
	<ComponentExample.Preview>
		<Input type="email" placeholder="email" class="max-w-xs" />
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Select</ComponentExample.Header>
	<ComponentExample.Preview>
		<Select.Root>
			<Select.Trigger class="w-[180px]">
				<Select.Value placeholder="Theme" />
			</Select.Trigger>
			<Select.Content>
				<Select.Item value="light">Light</Select.Item>
				<Select.Item value="dark">Dark</Select.Item>
				<Select.Item value="system">System</Select.Item>
			</Select.Content>
		</Select.Root>
	</ComponentExample.Preview>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header>Select</ComponentExample.Header>
	<ComponentExample.Preview>
		<div class="flex items-center space-x-2">
			<Switch id="airplane-mode" />
			<Label for="airplane-mode">Airplane Mode</Label>
		</div>
	</ComponentExample.Preview>
</ComponentExample>
