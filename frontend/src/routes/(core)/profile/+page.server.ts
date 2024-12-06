import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { tokenStoreSchema } from '$lib/stores/tokenStore';
import { UserApi } from '$lib/api/server';

export const load: PageServerLoad = async ({ cookies }) => {
	const accessToken = cookies.get(tokenStoreSchema.accessToken);

	if (!accessToken) {
		return redirect(302, '/login?redirect=/profile');
	}

	try {
		const data = await UserApi.getCurrentUser(cookies);
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
