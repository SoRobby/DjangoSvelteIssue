<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
	import { Button } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';
	import { EllipsisVertical, MapPin } from 'lucide-svelte';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import AddLocationDialog from './AddLocationDialog.svelte';
	import * as Dialog from '$lib/components/ui/dialog';
	import LocationCard from './LocationCard.svelte';
</script>

<div class="space-y-12">
	<section class="space-y-4">
		<div class="flex justify-between border-b pb-4">
			<div>
				<SupplierFormSection
					title="Locations"
					description="Manage your company's offices and facilities"
				/>
			</div>

			<div>
				<AddLocationDialog />
			</div>
		</div>

		<div class="grid grid-cols-2 gap-6">
			<div class="col-span-2 rounded-md border py-8 text-center text-muted">
				<MapPin size="36" class="mx-auto mb-2 opacity-50" />
				<p>No locations added yet</p>
			</div>

			<LocationCard isHeadquarters={true} />
			<LocationCard isHeadquarters={false} />
			<LocationCard isHeadquarters={false} />
		</div>
	</section>
</div>
