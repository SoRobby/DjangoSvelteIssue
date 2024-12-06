import { HelloWorldApi } from '$lib/api/client';

/** @type {import('./$types').Actions} */
export const actions = {
	default: async ({ request, cookies }) => {
		// Get form data
		const formData = await request.formData();
		let content = String(formData.get('content'));

		try {
			const data = HelloWorldApi.helloWorldPost(content);
			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}
	}
};
