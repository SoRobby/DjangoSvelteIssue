import type { Actions } from './$types';
import { UserSettingsApi } from '$lib/api/client';

export const actions = {
	submitSupportMessage: async ({ request, cookies }) => {
		// Get the form data directly from the request
		const formData = await request.formData();

		const name = formData.get('name') as string;
		const username = formData.get('username') as string;
		const email = formData.get('email') as string;
		const subject = formData.get('subject') as string;
		const content = formData.get('content') as string;

		// Make the API request
		try {
			const accessToken = cookies.get('accessToken') || '';
			const data = UserSettingsApi.sendSupportMessage(
				accessToken,
				name,
				username,
				email,
				subject,
				content
			);

			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}
	}
} satisfies Actions;
