<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { Separator } from '$lib/components/ui/separator';
	import SectionInputOutput from './SectionInputOutput.svelte';
	import { ToolHeader } from '$lib/components/apps/tools/tool-header';
	import SectionReport from './SectionReport.svelte';
	import SectionMethodology from './SectionMethodology.svelte';
	import SectionInstructions from './SectionInstructions.svelte';
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/tools">Tool Center</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>Add Two Numbers</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<!-- Header -->
<ToolHeader name="Add Two Numbers" />
<Separator />

<!-- Tool inputs -->
<SectionInputOutput />
<Separator />

<!-- Report -->
<SectionReport />
<Separator />

<!-- Methodology -->
<SectionMethodology />
<Separator />

<!-- Instructions -->
<SectionInstructions />
