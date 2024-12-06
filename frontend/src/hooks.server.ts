import type { Handle } from '@sveltejs/kit';
import UserApi from '$lib/api/server/user';
import { tokenStoreSchema } from '$lib/stores/tokenStore';

export const handle: Handle = async ({ event, resolve }) => {
	// Add any sort of hooks and middleware here

	// Get cookies from the request
	const cookies = event.cookies;

	// Get the JWT access token from cookies
	const accessToken = cookies.get(tokenStoreSchema.accessToken);

	// Initialize locals.user to ensure it's always defined
	event.locals.user = {};

	if (accessToken) {
		try {
			// Validate the token and fetch the user data from the API
			const data = await UserApi.getCurrentUser(cookies);

			// Populate event.locals.user with user information
			event.locals.user = {
				username: data.account.username,
				email: data.account.email,
				first_name: data.account.first_name,
				last_name: data.account.last_name,
				organization: data.account.organization || null,
				country_slug: data.account.country.slug || null,
				profile_image_thumbnail: data.account.profile_image_thumbnail || null,
				is_superuser: data.account.is_superuser,
				managed_suppliers: data.account.managed_suppliers
			};
		} catch (error) {
			// Log the error for debugging purposes
			console.error('[HOOKS.SERVER.TS] Error fetching user data:', error);

			// Clear invalid or expired tokens
			cookies.set(tokenStoreSchema.accessToken, '', {
				path: '/',
				expires: new Date(0)
			});

			// Ensure event.locals.user remains empty
			event.locals.user = {};
		}
	} else {
		console.info('[HOOKS.SERVER.TS] No access token found. User not logged in.');
	}

	// Proceed with resolving the request
	const response = await resolve(event);

	// Security headers for every response
	response.headers.set('X-Frame-Options', 'DENY');
	response.headers.set('X-Content-Type-Options', 'nosniff');
	response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');

	return response;
};
