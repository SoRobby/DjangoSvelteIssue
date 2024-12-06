<script lang="ts">
	import { PUBLIC_SITE_NAME } from '$env/static/public';
	import AuthHeading from '../AuthHeading.svelte';
	import { FieldContainer } from '$lib/components/layout/field-container';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Link } from '$lib/components/ui/link';
	import { Button } from '$lib/components/ui/button';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { LoaderCircle } from 'lucide-svelte';
	import api from '$lib/api/client/auth';

	// Form state
	let email: string = $state('');
	let password: string = $state('');
	let rememberMe: boolean = $state(false);
	let isSubmitting: boolean = $state(false);
	let formSuccess: boolean = $state(false);
	let formMessage: string = $state('');

	function validateForm() {
		const requiredInputs = Array.from(
			document.querySelectorAll('input[required]')
		) as HTMLInputElement[];

		const isFormValid = requiredInputs.every((input) => {
			const isValid = input.checkValidity();
			if (!isValid) input.reportValidity();
			return isValid;
		});

		return isFormValid;
	}

	async function authenticate(event: Event) {
		event.preventDefault();

		// Verify that all input fields have a valid value
		const isFormValid: boolean = validateForm();
		if (!isFormValid) {
			return;
		}

		// Submitting the form
		isSubmitting = true;
		try {
			let data = await api.login(email, password, rememberMe);

			if (data?.success) {
				// check the url to see if there is a redirect
				if (window.location.search.includes('redirect')) {
					const urlParams = new URLSearchParams(window.location.search);
					const redirect = urlParams.get('redirect');
					window.location.href = String(redirect);
				} else {
					window.location.href = '/';
				}
			} else {
				formMessage = data?.message ?? 'Invalid email and/or password';
				formSuccess = false;
				isSubmitting = false;
			}
		} catch (error) {
			console.error('[Login] Authentication failed:', error);
			formMessage = 'An error occurred during authentication';
			formSuccess = false;
		}
	}
</script>

<svelte:head>
	<title>Login | {PUBLIC_SITE_NAME}</title>
	<meta name="description" content="Login to {PUBLIC_SITE_NAME}" />
</svelte:head>

<div class="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
	<AuthHeading title="Sign in to your account" />
	<div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
		<div class="rounded-lg bg-white px-6 py-12 shadow sm:px-12">
			<form method="POST" onsubmit={authenticate} class="space-y-6">
				<FieldContainer>
					<Label for="email">Email address</Label>
					<Input type="email" name="email" id="email" bind:value={email} required maxlength={255} />
				</FieldContainer>

				<FieldContainer>
					<Label for="password">Password</Label>
					<Input type="password" name="password" id="password" bind:value={password} required maxlength={128} />
				</FieldContainer>

				<div class="flex items-center justify-between">
					<div class="flex items-center gap-x-1">
						<Checkbox id="remember-me" bind:checked={rememberMe} />
						<Label for="remember-me" class="text-tertiary hover:text-primary ml-2"
							>Remember me</Label
						>
					</div>

					<div>
						<Link href="/reset-password" class="text-sm">Forgot password?</Link>
					</div>
				</div>

				{#if !isSubmitting}
					<Button class="w-full" type="button" onclick={authenticate}>Sign in</Button>
				{:else}
					<Button disabled variant="ghost" class="w-full" type="button">
						<LoaderCircle class="mr-2 h-4 w-4 animate-spin" />
						Signing in...
					</Button>
				{/if}
			</form>

			<!-- Error message -->
			{#if formSuccess === false && formMessage.length > 0}
				<div class="flex justify-center">
					<p class="mt-4 text-sm font-medium text-destructive">{formMessage}</p>
				</div>
			{/if}
		</div>
		<p class="text-muted mt-10 text-center text-sm">
			Don't have an account?
			<Link href="/register">Create an account</Link>
		</p>
	</div>
</div>
