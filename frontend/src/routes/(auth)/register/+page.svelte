<script lang="ts">
	import { PUBLIC_SITE_NAME } from '$env/static/public';
	import AuthHeading from '../AuthHeading.svelte';
	import { Link } from '$lib/components/ui/link';
	import { Button } from '$lib/components/ui/button';
	import { FieldContainer } from '$lib/components/layout/field-container';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { LoaderCircle } from 'lucide-svelte';
	import CountryField from './CountryField.svelte';

	let { data } = $props();

	console.log(data);

	// Form step
	let formStep = $state('step-2');

	// Form fields
	let email = $state('');
	let username = $state('');
	let password1 = $state('');
	let password2 = $state('');
	let firstName = $state('');
	let lastName = $state('');
	let country = $state('');
	let organization = $state('');

	// Form validation state
	let isEmailValid = $state(false);
	let isEmailValidMessage = $state('');
	let isUsernameValid = $state(false);
	let isUsernameValidMessage = $state('');
	let isPassword1Valid = $state(false);
	let isPassword1ValidMessage = $state('');
	let isPassword2Valid = $state(false);
	let isPassword2ValidMessage = $state('');

	// Validation functions
	const validateEmail = async () => {
		// Check if email is empty
		if (!email && email.length === 0) {
			isEmailValid = true;
			isEmailValidMessage = '';
			return;
		}
	};

	const validateUsername = async () => {
		// Check if username is empty
		if (!username && username.length === 0) {
			isUsernameValid = true;
			isUsernameValidMessage = '';
			return;
		}
	};

	function changeToStep1() {
		formStep = 'step-1';
	}

	function changeToStep2() {
		// To change to step 2, validate fields in step 1
		const requiredInputs = Array.from(
			document.querySelectorAll('.step1-container input[required]')
		) as HTMLInputElement[]; // Explicitly cast to HTMLInputElement[]

		const inputsAreValid = requiredInputs.every((input) => {
			const isValid = input.checkValidity();
			if (!isValid) input.reportValidity();
			return isValid;
		});


		if (inputsAreValid && isEmailValid && isUsernameValid) {
			formStep = 'step-2';
		}
	}
</script>

<svelte:head>
	<title>Register - {PUBLIC_SITE_NAME}</title>
	<meta name="description" content="Get started by creating an account on {PUBLIC_SITE_NAME}" />
</svelte:head>

<div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
	<AuthHeading title="Create your account" />
	<div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[456px]">
		<div class="rounded-lg bg-white px-6 py-12 shadow sm:px-12">
			<form action="" class="space-y-6">
				<!-- Form steps -->
				<div class="grid grid-cols-2 gap-6">
					<button type="button" class="space-y-2 text-left" onclick={changeToStep1}>
						<div class="h-1 w-full rounded-full bg-blue-600"></div>
						<div class="text-sm font-medium text-brand">Step 1</div>
					</button>

					<button
						type="button"
						class="group space-y-2 text-left"
						onclick={changeToStep2}
					>
						<div class="h-1 w-full rounded-full bg-slate-200 group-hover:bg-slate-300"></div>
						<div class="text-sm font-medium text-muted group-hover:text-primary">Step 2</div>
					</button>
				</div>

				<!-- step 1 -->
				<div class="space-y-6 {formStep === 'step-1' ? '' : 'hidden'}">
					<FieldContainer class="step1-container">
						<Label for="email">Email address</Label>
						<Input
							type="email"
							name="email"
							id="email"
							maxlength={255}
							required
							bind:value={email}
						/>
					</FieldContainer>

					<FieldContainer class="step1-container">
						<Label for="username">Username</Label>
						<Input
							type="text"
							name="username"
							id="username"
							minlength={4}
							maxlength={16}
							required
							bind:value={username}
						/>
					</FieldContainer>

					<FieldContainer class="step1-container">
						<Label for="password1">Password</Label>
						<Input
							type="password"
							name="password1"
							id="password1"
							maxlength={128}
							required
							bind:value={password1}
						/>
					</FieldContainer>

					<FieldContainer class="step1-container">
						<Label for="password2">Confirm password</Label>
						<Input
							type="password"
							name="password2"
							id="password2"
							maxlength={128}
							required
							bind:value={password2}
						/>
					</FieldContainer>

					<Button size="sm" class="w-full" onclick={changeToStep2}>Continue</Button>
				</div>

				<!-- step 2 -->
				<div class="space-y-6 {formStep === 'step-2' ? '' : 'hidden'}">
					<FieldContainer class="step2-container">
						<Label for="first-name">First name</Label>
						<Input
							type="text"
							name="first-name"
							id="first-name"
							maxlength={120}
							required
							bind:value={firstName}
						/>
					</FieldContainer>

					<FieldContainer class="step2-container">
						<Label for="last-name">Last name</Label>
						<Input
							type="text"
							name="last-name"
							id="last-name"
							maxlength={120}
							required
							bind:value={lastName}
						/>
					</FieldContainer>

					<FieldContainer class="step2-container">
						<Label for="country">Country</Label>
						<CountryField countries={data.countries} />
						<!-- <Input type="text" name="country" id="country" required bind:value={country} /> -->
					</FieldContainer>

					<FieldContainer class="step2-container">
						<Label for="organization">Organization</Label>
						<Input
							type="text"
							name="organization"
							id="organization"
							maxlength={255}
							required
							bind:value={organization}
						/>
					</FieldContainer>

					<Button size="sm" class="w-full">Create account</Button>
					<Button disabled variant="ghost" class="w-full" type="button" size="sm">
						<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
						Launching account...
					</Button>
				</div>
			</form>
		</div>
		<p class="mt-10 text-center text-sm text-muted">
			Already have an account?
			<Link href="/login">Login here</Link>
		</p>
	</div>
</div>
