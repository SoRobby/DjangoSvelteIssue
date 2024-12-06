import type { PageServerLoad } from './$types';
import { SupplierApi } from '$lib/api/client';

export const load: PageServerLoad = async ({ params }) => {
	try {
		const data = await SupplierApi.getSupplier(params.supplier);
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
