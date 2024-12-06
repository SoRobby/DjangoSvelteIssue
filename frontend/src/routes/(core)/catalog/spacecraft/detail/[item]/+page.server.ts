import type { Actions } from './$types';
import type { PageServerLoad } from './$types';
import { InquiryApi, CountriesApi, CatalogApi } from '$lib/api/client';

export const load: PageServerLoad = async ({ params }) => {
	// Get list of all countries
	try {
		const itemData = await CatalogApi.getCatalogItem('spacecraft', params.item);
		const countryData = await CountriesApi.getCountries();
		const combinedData = { ...itemData, ...countryData };
		return combinedData;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};

function formatRequestCheckboxValue(value: string | null): boolean {
	if (value === 'on') {
		return true;
	}
	return false;
}

export const actions = {
	submitItemInquiry: async ({ request, cookies }) => {
		// Get the form data directly from the request

		// Get slug form URL
		// TODO need to fix this:
		const itemSlug = 'rocket-01';

		const formData = await request.formData();

		const fields = {
			name: formData.get('name') as string,
			username: formData.get('username') as string,
			email: formData.get('email') as string,
			organization: formData.get('organization') as string,
			position: null,
			countrySlug: formData.get('country') as string,
			content: formData.get('content') as string
		};

		// Checkbox fields
		const checkboxFields = [
			'request-datasheet',
			'request-icd',
			'request-options-sheet',
			'request-user-manual',
			'request-cad-model',
			'request-quotation',
			'request-lead-time',
			'request-heritage'
		];

		// Convert checkbox fields
		const checkboxValues = Object.fromEntries(
			checkboxFields.map((field) => [
				field,
				formatRequestCheckboxValue(formData.get(field) as string | null)
			])
		);

		// Attempt to get accessToken from cookies
		try {
			const accessToken = cookies.get('accessToken') || null;
			const data = await InquiryApi.submitItemInquiry(
				accessToken,
				itemSlug,
				fields.username,
				fields.name,
				fields.email,
				fields.organization,
				fields.position,
				fields.countrySlug,
				fields.content,

				checkboxValues['request-datasheet'],
				checkboxValues['request-icd'],
				checkboxValues['request-options-sheet'],
				checkboxValues['request-user-manual'],
				checkboxValues['request-cad-model'],
				checkboxValues['request-quotation'],
				checkboxValues['request-lead-time'],
				checkboxValues['request-heritage']
			);

			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}
	}
} satisfies Actions;
