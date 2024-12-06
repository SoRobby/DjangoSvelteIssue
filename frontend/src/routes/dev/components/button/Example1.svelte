<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
	import { Button } from '$lib/components/ui/button';

	const code = `<Button size="xs">Extra Small (h=32px)</Button>
<Button size="sm">Small (h=36px)</Button>
<Button size="default">Default (h=40px)</Button>
<Button size="lg">Large (h=44px)</Button>
<Button size="xl">Extra Large (h=48px)</Button>`;
</script>

<ComponentExample>
	<ComponentExample.Header {code}>Button Sizes</ComponentExample.Header>
	<ComponentExample.Description>
		A default link component to create uniform links across the application.
	</ComponentExample.Description>
	<ComponentExample.Preview>
		<div class="flex items-end space-x-4">
			<Button size="xs">Extra Small (h=32px)</Button>
			<Button size="sm">Small (h=36px)</Button>
			<Button size="default">Default (h=40px)</Button>
			<Button size="lg">Large (h=44px)</Button>
			<Button size="xl">Extra Large (h=48px)</Button>
		</div>
	</ComponentExample.Preview>
	<ComponentExample.Code {code}></ComponentExample.Code>
</ComponentExample>
