<script lang="ts">
	import { ToolCard } from '$lib/components/apps/tools/tool-card';
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { Input } from '$lib/components/ui/input';
	import { Separator } from '$lib/components/ui/separator';
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>Tool Center</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<!-- Header -->
<div class="flex justify-between items-center gap-x-6 pb-6">
	<div>
		<h1 class="text-xl font-medium">Tool Center</h1>
	</div>
	<div class="flex justify-center">
		<Input type="search" placeholder="Search for tool..." class="w-96" />
	</div>
</div>

<Separator />

<!-- Tools list -->
<div class="grid grid-cols-3 gap-6 py-6">
	<ToolCard title="Add Two Numbers" description="Test model that adds two numbers together, exercising the model's ability" href="/tools/tool" isPremium={false} />
	<ToolCard title="Add Three Numbers" description="Test model that adds two numbers together, exercising the model's ability" href="/tools/tool" isPremium={false} />
	<ToolCard title="Add Four Numbers" description="Test model that adds two numbers together, exercising the model's ability" href="/tools/tool" isPremium={false} />
</div>
