<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
	import { Button } from '$lib/components/ui/button';

	const code = `<p>This is the preview section where the main content goes.</p>`;
</script>

<ComponentExample>
	<ComponentExample.Header {code}>Button Variants</ComponentExample.Header>
	<ComponentExample.Description>
		A default link component to create uniform links across the application.
	</ComponentExample.Description>
	<ComponentExample.Preview>
		<div class="flex items-end space-x-4">
			<Button>Default</Button>
			<Button variant="outline">Outline</Button>
			<Button variant="secondary">Secondary</Button>
			<Button variant="ghost">Ghost</Button>
			<Button variant="destructive">Destructive</Button>
		</div>
	</ComponentExample.Preview>
	<ComponentExample.Code {code}></ComponentExample.Code>
</ComponentExample>


