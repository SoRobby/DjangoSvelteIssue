<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';

	const code = `<p>This is the preview section where the main content goes.</p>`;
</script>

<ComponentExample>
	<ComponentExample.Header {code}>Untitled</ComponentExample.Header>
	<ComponentExample.Description>
		A default link component to create uniform links across the application.
	</ComponentExample.Description>
	<ComponentExample.Preview>TBD</ComponentExample.Preview>
	<ComponentExample.Code {code}></ComponentExample.Code>
</ComponentExample>
