import type { Actions } from './$types';
import { UserSettingsApi } from '$lib/api/client';


export const actions = {
	default: async ({ request, cookies }) => {
        console.log('[UserSettingsApi] sendSupportMessage()');

        // Get the form data directly from the request
		const formData = await request.formData();

        function convertSwitchValueToBoolean(value: string | null) {
            if (value === 'on') {
                return true;
            } else {
                return false;
            }
        }

		// Emails
		let receiveMarketingEmails = convertSwitchValueToBoolean(
			formData.get('receive-marketing-emails') as string
		);
		let receiveWeeklyDigestEmails = convertSwitchValueToBoolean(
			formData.get('receive-weekly-digest-emails') as string
		);
		let receiveDiscoveryEmails = convertSwitchValueToBoolean(
			formData.get('receive-discovery-emails') as string
		);
		let receiveSiteUpdateEmails = convertSwitchValueToBoolean(
			formData.get('receive-site-update-emails') as string
		);

		// Notifications
		let receiveInboxMessageNotifications = convertSwitchValueToBoolean(
			formData.get('receive-inbox-message-notifications') as string
		);
		let receiveAnnouncementNotifications = convertSwitchValueToBoolean(
			formData.get('receive-announcement-notifications') as string
		);


		// Make the API request
		try {
			const accessToken = cookies.get('accessToken') || '';
			const data = UserSettingsApi.editAccountNotifications(
				accessToken,
				receiveMarketingEmails,
				receiveWeeklyDigestEmails,
				receiveDiscoveryEmails,
				receiveSiteUpdateEmails,
				receiveInboxMessageNotifications,
				receiveAnnouncementNotifications
			);

			return data;
		} catch (error) {
			console.error('An error occurred:', error);
			throw error;
		}
	}
} satisfies Actions;
