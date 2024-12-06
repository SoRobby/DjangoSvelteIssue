<script lang="ts">
	import { Badge } from '$lib/components/ui/badge';
	import { MoveRight } from 'lucide-svelte';
</script>

<div class="grid grid-cols-12 gap-12 rounded-md p-4">
	<div class="col-span-12 items-center space-y-4 md:col-span-5 md:pt-8">
		<Badge>Supplier Program</Badge>
		<h1 class="text-4xl font-bold text-primary">JOIN....</h1>
		<p class="text-2xl text-tertiary">
			Reach more customers [insert better tagline]
		</p>
		<div class="pt-4">
			<a
				href="/supplier-program/register"
				class="flex w-min items-center gap-x-2 text-nowrap text-lg font-medium text-brand hover:text-blue-800 hover:underline"
				>Join today
				<MoveRight class="h-5 w-5" />
			</a>
		</div>
	</div>
</div>

