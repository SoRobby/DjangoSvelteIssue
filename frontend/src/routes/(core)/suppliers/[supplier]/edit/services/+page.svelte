<script lang="ts">
	import SupplierFormSection from '../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
    import { Link } from '$lib/components/ui/link';
	import { View } from 'lucide-svelte';
</script>

<div class="space-y-12">
	<section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="Services" description="Basic information about your company" />
		</div>
	</section>
</div>

