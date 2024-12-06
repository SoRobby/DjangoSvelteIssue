import type { PageServerLoad } from './$types';
import { SupplierApi, UserSettingsApi } from '$lib/api/client';

export const actions = {
	default: async ({ params, request, cookies }) => {
		// Get the form data directly from the request
		const formData = await request.formData();

		console.log(formData);

		const metaTitle = formData.get('meta-title') as string;
		const metaDescription = formData.get('meta-description') as string;
		const metaKeywords = formData.get('meta-keywords') as string;

		// Make the API request
		try {
			const accessToken = cookies.get('accessToken') || '';
            console.log(accessToken);
            
			const data = SupplierApi.updateSupplierSEO(
				accessToken,
				params.supplier,
				metaTitle,
				metaDescription,
				metaKeywords
			);

			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}

		// const firstName = formData.get('first-name') as string;
		// const lastName = formData.get('last-name') as string;
		// const bio = formData.get('bio') as string;
		// const organization = formData.get('organization') as string;
		// const position = formData.get('position') as string;
		// const countrySlug = formData.get('countrySlug') as string;

		// const profileImage = formData.get('profile-image-file') as File | null;
		// const croppedImageDetails = {
		// 	x: Number(formData.get('cropped-image-x')),
		// 	y: Number(formData.get('cropped-image-y')),
		// 	width: Number(formData.get('cropped-image-width')),
		// 	height: Number(formData.get('cropped-image-height'))
		// }

		// // Make the API request
		// try {
		// 	const accessToken = cookies.get('accessToken') || '';
		// 	const data = UserSettingsApi.editAccountGeneral(
		// 		accessToken,
		// 		firstName,
		// 		lastName,
		// 		bio,
		// 		organization,
		// 		position,
		// 		countrySlug,
		// 		// profileImage,
		// 		// croppedImageDetails
		// 	);

		// 	return data;
		// } catch (error) {
		// 	console.error('An error occurred:', error);
		// 	throw error;
		// }
	}
};
