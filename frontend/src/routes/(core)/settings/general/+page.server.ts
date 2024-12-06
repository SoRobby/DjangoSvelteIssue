import type { PageServerLoad } from './$types';
import { CountriesApi, UserSettingsApi } from '$lib/api/client';

export const load: PageServerLoad = async ({ params }) => {
	// Get list of all countries
	try {
		const data = await CountriesApi.getCountries();
		return data;
	} catch (error) {
		console.error('An error occurred:', error);
		throw error;
	}
};



export const actions = {
	default: async ({ request, cookies }) => {
		// Get the form data directly from the request
		const formData = await request.formData();

		console.log(formData);

		const firstName = formData.get('first-name') as string;
		const lastName = formData.get('last-name') as string;
		const bio = formData.get('bio') as string;
		const organization = formData.get('organization') as string;
		const position = formData.get('position') as string;
		const countrySlug = formData.get('countrySlug') as string;

		const profileImage = formData.get('profile-image-file') as File | null;
		const croppedImageDetails = {
			x: Number(formData.get('cropped-image-x')),
			y: Number(formData.get('cropped-image-y')),
			width: Number(formData.get('cropped-image-width')),
			height: Number(formData.get('cropped-image-height'))
		}

		// Make the API request
		try {
			const accessToken = cookies.get('accessToken') || '';
			const data = UserSettingsApi.editAccountGeneral(
				accessToken,
				firstName,
				lastName,
				bio,
				organization,
				position,
				countrySlug,
				// profileImage,
				// croppedImageDetails
			);

			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}

	}

}



