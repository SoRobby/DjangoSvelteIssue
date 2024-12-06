import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
import { isObjectEmpty } from '$lib/utils/isObjectEmpty';

export const load: PageServerLoad = async ({ locals }) => {
	// If user is already logged in, redirect to home page
	if (!isObjectEmpty(locals.user)) {
		return redirect(302, '/');
	}
};
