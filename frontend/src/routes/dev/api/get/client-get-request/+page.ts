import { HelloWorldApi } from '$lib/api/client';

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
	console.log('[API TEST] Client get request');
	try {
		const data = HelloWorldApi.helloWorldGet();
		return data;
	} catch (error) {
		console.log('[API TEST] Error:', error);
		return error;
	}
}
