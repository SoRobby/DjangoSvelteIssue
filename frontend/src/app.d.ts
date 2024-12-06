// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		interface Locals {
			user?: {
				username: string;
				email: string;
				first_name: string
				last_name: string;
				profile_image_thumbnail?: string
				country_slug: string;
				is_superuser: boolean;
			} | {};
		}

		// interface Error {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
}

export {};
