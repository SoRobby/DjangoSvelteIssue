<script lang="ts">
	import SupplierFormSection from './SupplierFormSection.svelte';
	import { Label } from '$lib/components/ui/label';
	import { FieldContainerX } from '$lib/components/layout/field-container-x';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Skeleton } from '$lib/components/ui/skeleton';

	// Form state
	let isSubmitting: boolean = $state(false);
	let isSaved: boolean = $state(true);
</script>


<div class="grid grid-cols-12 gap-4">
    <div class="col-span-12">
        <Skeleton class="rounded-md w-full h-64" />
    </div>

    <div class="col-span-3">
        <Skeleton class="rounded-md w-full h-32" />
    </div>

    <div class="col-span-3">
        <Skeleton class="rounded-md w-full h-32" />
    </div>

    <div class="col-span-3">
        <Skeleton class="rounded-md w-full h-32" />
    </div>

    <div class="col-span-3 border rounded-md">
		<h3>TBD</h3>
		<p>52</p>
    </div>


    <div class="col-span-6">
        <Skeleton class="rounded-md w-full h-64" />
    </div>

    <div class="col-span-6">
        <Skeleton class="rounded-md w-full h-64" />
    </div>
</div>




