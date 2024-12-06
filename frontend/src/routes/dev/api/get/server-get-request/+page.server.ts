import { HelloWorldApi } from '$lib/api/client';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
	console.log('[API TEST] Server get request');
	try {
		const data = HelloWorldApi.helloWorldGet();
		return data;
	} catch (error) {
		console.log('[API TEST] Error:', error);
		return error;
	}
}
