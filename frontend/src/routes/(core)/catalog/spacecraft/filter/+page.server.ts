import { CatalogApi } from '$lib/api/client';

import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	try {
		const data = await CatalogApi.getCatalogRootNodesWithChildren('spacecraft');
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
