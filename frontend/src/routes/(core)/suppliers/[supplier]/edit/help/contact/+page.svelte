<script lang="ts">
	import SupplierFormSection from '../../SupplierFormSection.svelte';
	import FieldContainer from '$lib/components/layout/field-container/field-container.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import { Textarea } from '$lib/components/ui/textarea';
    import { Link } from '$lib/components/ui/link';
	import { View } from 'lucide-svelte';
	import * as Alert from '$lib/components/ui/alert';
	import { Button } from '$lib/components/ui/button';
</script>

<div class="space-y-12">
	<section class="space-y-4">
		<div class="border-b pb-4">
			<SupplierFormSection title="Support" description="Our support team will reach out to you at the earliest opportunity to assist with your request" />
		</div>

		<div>
			<div class="space-y-2 text-sm">
				<div class="grid grid-cols-6 gap-4 pt-4 md:grid-cols-12 md:gap-8">
					<FieldContainer class="col-span-6">
						<Label for="name">Name</Label>
						<Input type="text" id="name" name="name" required />
					</FieldContainer>
	
					<FieldContainer class="col-span-6">
						<Label for="email">Email address</Label>
						<Input type="email" id="email" name="email" required />
					</FieldContainer>
				</div>
	
				<FieldContainer class="pt-4">
					<Label for="subject">Subject</Label>
					<Input type="text" id="subject" name="subject" required />
				</FieldContainer>
	
				<FieldContainer class="pt-4">
					<Label for="content">Message</Label>
					<Textarea id="content" name="content" required />
				</FieldContainer>
			</div>

			<div class="flex flex-row items-center justify-end gap-4 pt-4">
				<Button type="button" variant="ghost" size="sm">Cancel</Button>
				<Button type="submit" size="sm">Send message</Button>
			</div>

			<Alert.Root class="mt-4 bg-green-50 text-green-800">
				<Alert.Title>Support message sent</Alert.Title>
				<Alert.Description>
					Your support message was successfully sent. Our team will reach out to you at the
					earliest opportunity to assist with your request.
				</Alert.Description>
			</Alert.Root>
		</div>
	</section>
</div>

