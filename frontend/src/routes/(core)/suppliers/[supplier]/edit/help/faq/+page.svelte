<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Link } from '$lib/components/ui/link';
	import { View } from 'lucide-svelte';
	import * as Accordion from '$lib/components/ui/accordion';
</script>

<div class="space-y-12">
	<section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="FAQ" description="Frequently asked questions" />
		</div>

		<div>
			<Accordion.Root class="-mt-4">
				<Accordion.Item value="item-1">
					<Accordion.Trigger>How can I restrict which counties can view my products?</Accordion.Trigger>
					<Accordion.Content>Yes. It adheres to the WAI-ARIA design pattern.</Accordion.Content>
				</Accordion.Item>
				<Accordion.Item value="item-2">
					<Accordion.Trigger>How can I add new admin users to help manage the company profile?</Accordion.Trigger>
					<Accordion.Content>Yes. It adheres to the WAI-ARIA design pattern.</Accordion.Content>
				</Accordion.Item>
			</Accordion.Root>
		</div>
	</section>
</div>


