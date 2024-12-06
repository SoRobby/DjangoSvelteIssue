<script lang="ts">
	import { Label } from '$lib/components/ui/label';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select/index.js';
	import { FieldContainer } from '$lib/components/layout/field-container';

	import { ToolInputCard } from '$lib/components/apps/tools/tool-input-card';
	import { ToolOutputCard } from '$lib/components/apps/tools/tool-output-card';
	import { ToolOutputRow } from '$lib/components/apps/tools/tool-output-row';
	import { ToolInputOutputCard } from '$lib/components/apps/tools/tool-input-output-card';
	import { ToolInputHelpText } from '$lib/components/apps/tools/tool-input-help-text';
</script>

<ToolInputOutputCard>
	<ToolInputCard>
		<FieldContainer class="grid grid-cols-8 items-center gap-x-4 gap-y-1 pt-4">
			<div class="col-span-2">
				<Label>Central body</Label>
			</div>
			<div class="col-span-6">
				<Select.Root type="single">
					<Select.Trigger class="w-full">Earth</Select.Trigger>
					<Select.Content>
						<Select.Item value="sun">Sun</Select.Item>
						<Select.Item value="mercury">Mercury</Select.Item>
						<Select.Item value="venus">Venus</Select.Item>
						<Select.Item value="earth">Earth</Select.Item>
						<Select.Item value="moon">Moon</Select.Item>
						<Select.Item value="mars">Mars</Select.Item>
						<Select.Item value="jupiter">Jupiter</Select.Item>
						<Select.Item value="saturn">Saturn</Select.Item>
						<Select.Item value="uranus">Uranus</Select.Item>
						<Select.Item value="neptune">Neptune</Select.Item>
						<Select.Item value="custom">Custom</Select.Item>
					</Select.Content>
				</Select.Root>
			</div>
			<div class="col-span-6 col-start-3 text-xs">
				<ToolInputHelpText variant="default"
					>Central body the satellite is orbiting.</ToolInputHelpText
				>
			</div>
		</FieldContainer>

		<FieldContainer class="grid grid-cols-8 items-center gap-x-4 gap-y-1 pt-4">
			<div class="col-span-2">
				<Label>Perigee altitude</Label>
			</div>
			<div class="col-span-6">
				<div class="relative">
					<Input type="number" class="w-full pr-10" value={450} />
					<div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
						<span class="text-sm text-muted">km</span>
					</div>
				</div>
			</div>
			<div class="col-span-6 col-start-3 text-xs">
				<ToolInputHelpText variant="default"
					>Closest distance from surface of central body to satellite.</ToolInputHelpText
				>
				<ToolInputHelpText variant="warning"
					>Perigee altitude is too low and will eventually result in satellite re-entry.</ToolInputHelpText
				>
				<ToolInputHelpText variant="error"
					>Perigee altitude must be less than apogee altitude.</ToolInputHelpText
				>
			</div>
		</FieldContainer>

		<FieldContainer class="grid grid-cols-8 items-center gap-x-4 gap-y-1 pt-4">
			<div class="col-span-2">
				<Label>Apogee altitude</Label>
			</div>
			<div class="col-span-6">
				<div class="relative">
					<Input type="number" class="w-full pr-10" value={500} />
					<div class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
						<span class="text-sm text-muted">km</span>
					</div>
				</div>
			</div>
			<div class="col-span-6 col-start-3 text-xs">
				<ToolInputHelpText variant="default"
					>Furthest distance from surface of central body to satellite.</ToolInputHelpText
				>
			</div>
		</FieldContainer>
	</ToolInputCard>
	<ToolOutputCard>
		<ToolOutputRow name="Power generated at Earth" value="1361 m/m^2" />
		<ToolOutputRow name="Power generated at location" value="526 m/m^2" />
	</ToolOutputCard>
</ToolInputOutputCard>
