<script lang="ts">
	import * as Breadcrumb from '$lib/components/ui/breadcrumb';
	import { Label } from '$lib/components/ui/label';
	import * as Pagination from "$lib/components/ui/pagination";
	import { Input } from '$lib/components/ui/input';
	import { Edit } from 'lucide-svelte';
    import { Link } from '$lib/components/ui/link';
	import SupplierBanner from './SupplierBanner.svelte';

	let { data } = $props();
</script>

<!-- Breadcrumb navigation -->
<Breadcrumb.Root class="pb-4 sm:pb-6">
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Home</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Link href="/">Suppliers</Breadcrumb.Link>
		</Breadcrumb.Item>
		<Breadcrumb.Separator>/</Breadcrumb.Separator>
		<Breadcrumb.Item>
			<Breadcrumb.Page>{data.supplier.name}</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>

<SupplierBanner supplier={data.supplier} />