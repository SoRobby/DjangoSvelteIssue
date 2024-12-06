<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
</script>

<div>
	<h2 class="pb-2 text-2xl font-bold text-gray-800">Dev Page</h2>
	<p class="text-gray-700">This is a short description of the dev page...</p>
</div>

<ComponentExample>
	<ComponentExample.Header code={'code'}>TBD</ComponentExample.Header>
	<ComponentExample.Description>my description...</ComponentExample.Description>
	<ComponentExample.Preview>xxxx</ComponentExample.Preview>
	<ComponentExample.Code code={'code'}></ComponentExample.Code>
</ComponentExample>

<ComponentExample>
	<ComponentExample.Header code="Example code snippet">This is the Header</ComponentExample.Header>
	<ComponentExample.Description>
		This is a description for the component example.
	</ComponentExample.Description>
	<ComponentExample.Preview>
		<p>This is the preview section where the main content goes.</p>
	</ComponentExample.Preview>
	<ComponentExample.Code
		code="<p>This is the preview section where the main content goes.</p>"
	></ComponentExample.Code>
</ComponentExample>
