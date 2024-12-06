<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
</script>

<div class="space-y-12">
	<section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="Overview" description="Basic information about your company" />
		</div>
		<div class="grid grid-cols-12 gap-6">
			<FieldContainer class="col-span-8">
				<Label for="company-name">Company name</Label>
				<Input type="text" name="company-name" id="company-name" required />
			</FieldContainer>

			<FieldContainer class="col-span-4">
				<Label for="company-name">Acronym</Label>
				<Input type="text" name="company-name" id="company-name" placeholder="e.g., NASA" required />
			</FieldContainer>

			<FieldContainer class="col-span-12">
				<Label for="company-name">Tagline</Label>
				<Input type="text" name="company-name" id="company-name" required />
			</FieldContainer>


			<FieldContainer class="col-span-8">
				<Label for="company-name">Website</Label>
				<Input type="text" name="company-name" id="company-name" required />
			</FieldContainer>

            <div class="col-span-4">
                <FieldContainer>
                    <Label for="company-name">Logo</Label>
                    <Input type="file" name="company-name" id="company-name" required />
                </FieldContainer>
            </div>

			<FieldContainer class="col-span-12">
				<Label for="company-name">Company description</Label>
                <Textarea></Textarea>
			</FieldContainer>
		</div>
	</section>

	<section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="Company Details" description="Additional information about your organization" />
		</div>
		<div class="grid grid-cols-12 gap-6">
			<FieldContainer class="col-span-3">
				<Label for="year-founded">Year founded</Label>
				<Input type="number" min={1900} name="year-founded" id="year-founded" placeholder="YYYY" required />
			</FieldContainer>
			<FieldContainer class="col-span-3">
				<Label for="number-of-employees">Number of employees</Label>
				<Input type="text" name="number-of-employees" id="number-of-employees" required />
			</FieldContainer>
			<FieldContainer class="col-span-6">
				<Label for="company-name">Specialization tags</Label>
				<Input type="text" name="company-name" id="company-name" required />
			</FieldContainer>
            <div class="bg-red-100 text-red-800 col-span-12 p-2 rounded-md">
                <p>Add section for uploading company documents (e.g., company overview)</p>
            </div>
		</div>
	</section>


    <section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="Social Media" description="Connect your social media profiles to increase awareness" />
		</div>
		<div class="grid grid-cols-12 gap-6">

            <div class="col-span-12 grid grid-cols-8 items-center">
                <div class="col-span-1">
                    <Label for="first-name">LinkedIn</Label>
                </div>
                <div class="col-span-7">
                    <Input type="text" name="first-name" id="first-name" class="max-w-full" required />
                </div>
            </div>

            <div class="col-span-12 grid grid-cols-8 items-center">
                <div class="col-span-1">
                    <Label for="first-name">Facebook</Label>
                </div>
                <div class="col-span-7">
                    <Input type="text" name="first-name" id="first-name" class="max-w-full" required />
                </div>
            </div>

            <div class="col-span-12 grid grid-cols-8 items-center">
                <div class="col-span-1">
                    <Label for="first-name">Instagram</Label>
                </div>
                <div class="col-span-7">
                    <Input type="text" name="first-name" id="first-name" class="max-w-full" required />
                </div>
            </div>

            <div class="col-span-12 grid grid-cols-8 items-center">
                <div class="col-span-1">
                    <Label for="first-name">X (Twitter)</Label>
                </div>
                <div class="col-span-7">
                    <Input type="text" name="first-name" id="first-name" class="max-w-full" required />
                </div>
            </div>

            <div class="col-span-12 grid grid-cols-8 items-center">
                <div class="col-span-1">
                    <Label for="first-name">YouTube</Label>
                </div>
                <div class="col-span-7">
                    <Input type="text" name="first-name" id="first-name" class="max-w-full" required />
                </div>
            </div>
		</div>
	</section>
</div>
