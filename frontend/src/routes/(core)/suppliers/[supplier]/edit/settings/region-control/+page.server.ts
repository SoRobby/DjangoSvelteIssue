import type { PageServerLoad } from './$types';
import { CountriesApi } from '$lib/api/client';


export const load: PageServerLoad = async ({ params }) => {
	try {
		const data = await CountriesApi.getCountries();
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};