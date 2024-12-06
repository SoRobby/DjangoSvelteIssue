import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { CountriesApi } from '$lib/api/client';
import { isObjectEmpty } from '$lib/utils/isObjectEmpty';

export const load: PageServerLoad = async ({ locals }) => {
	if (!isObjectEmpty(locals.user)) {
		return redirect(302, '/');
	}

	try {
		const data = await CountriesApi.getCountries();
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
