<script lang="ts">
	import { ComponentExample } from '$lib/components/dev/component-example';
</script>

<div>
	<h2 class="pb-2 text-2xl font-bold text-gray-800">Dev Page</h2>
	<p class="text-gray-700">This is a short description of the dev page...</p>
</div>


<ComponentExample>
	<ComponentExample.Header code="Example code snippet">Link</ComponentExample.Header>
	<ComponentExample.Description>
		A default link component to create uniform links across the application.
	</ComponentExample.Description>
	<ComponentExample.Preview>
        TBD
	</ComponentExample.Preview>
	<ComponentExample.Code
		code="<p>This is the preview section where the main content goes.</p>"
	></ComponentExample.Code>
</ComponentExample>
