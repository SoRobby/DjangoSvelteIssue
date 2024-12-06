export async function load({ locals }) {
	// Pass the user data to +page.svelte
	console.log('This is an example.... updating +layout.server.ts');
	let a = 1;
	let b = 2;
	let c = a + b;

	return {
		user: locals.user
	};
}
