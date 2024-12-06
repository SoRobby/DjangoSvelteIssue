<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb/index.js';

	const code = `<p>This is the preview section where the main content goes.</p>`;
</script>

<ComponentExample>
	<ComponentExample.Header {code}>Default</ComponentExample.Header>
	<ComponentExample.Description>
		<Breadcrumb.Root>
			<Breadcrumb.List>
				<Breadcrumb.Item>
					<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
				</Breadcrumb.Item>
				<Breadcrumb.Separator />
				<Breadcrumb.Item>
					<Breadcrumb.Link href="/">Components</Breadcrumb.Link>
				</Breadcrumb.Item>
				<Breadcrumb.Separator />
				<Breadcrumb.Item>
					<Breadcrumb.Page>Breadcrumb</Breadcrumb.Page>
				</Breadcrumb.Item>
			</Breadcrumb.List>
		</Breadcrumb.Root>
	</ComponentExample.Description>
	<ComponentExample.Preview>TBD</ComponentExample.Preview>
	<ComponentExample.Code {code}></ComponentExample.Code>
</ComponentExample>
