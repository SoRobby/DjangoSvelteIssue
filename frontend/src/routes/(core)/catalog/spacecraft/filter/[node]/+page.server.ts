import { CatalogApi } from '$lib/api/client';

import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	// Get current node
	const node = params.node;
	console.log(node);

	try {
		const data = await CatalogApi.getCatalogNodesWithChildrenAndItems('spacecraft', node);
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};
