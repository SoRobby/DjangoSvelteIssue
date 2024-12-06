import type { PageServerLoad } from './$types';
import { SupplierApi } from '$lib/api/client';

export const load: PageServerLoad = async ({ url }) => {
	const page = parseInt(url.searchParams.get('page') || '1');
	const countries = url.searchParams.getAll('countries') || [];

	try {
		const data = await SupplierApi.getSuppliers(page, countries);
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};

