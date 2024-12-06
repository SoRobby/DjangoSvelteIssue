<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
	import Badge from '$lib/components/ui/badge/badge.svelte';

	const code = `<p>This is the preview section where the main content goes.</p>`;
</script>

<ComponentExample>
	<ComponentExample.Header {code}>Shapes</ComponentExample.Header>
	<ComponentExample.Description>
		A default link component to create uniform links across the application.
	</ComponentExample.Description>
	<ComponentExample.Preview>
		<Badge shape="pill">Pill (Default)</Badge>
		<Badge shape="square">Square</Badge>
	</ComponentExample.Preview>
	<ComponentExample.Code {code}></ComponentExample.Code>
</ComponentExample>
