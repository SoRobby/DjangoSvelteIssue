import type { LayoutServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { tokenStoreSchema } from '$lib/stores/tokenStore';
import { UserApi } from '$lib/api/server';
import { UserSettingsApi, SupplierApi } from '$lib/api/client';

export const load: LayoutServerLoad = async ({ cookies, params }) => {
	const accessToken = cookies.get(tokenStoreSchema.accessToken);

	if (!accessToken) {
		return redirect(302, '/login?redirect=/profile/settings');
	}

	try {
		// const data = await UserApi.getCurrentUser(cookies);
		const accessToken = cookies.get(tokenStoreSchema.accessToken) as string;
		// const data = await UserSettingsApi.getAccount(accessToken)

		const data = await SupplierApi.getSupplierProfileAdmin(params.supplier);
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
