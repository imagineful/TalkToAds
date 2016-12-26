from bingads.v10.bulk import *
from bingads.reporting import *


class BingAdsService(object):
    def __init__(self, account_info):
        self._campaign_service = None
        self._reporting_service = None
        self._bulk_service = None
        self._bulk_service_manager = None
        self._account_info = account_info
        self._initialize()

    def _initialize(self):
        authentication = OAuthDesktopMobileAuthCodeGrant(client_id=self.account_info.client_id)
        authentication.request_oauth_tokens_by_refresh_token(self.account_info.refresh_token)
        auth = AuthorizationData(
            account_id=self.account_info.account_id,
            customer_id=self.account_info.customer_id,
            developer_token=self.account_info.developer_token,
            authentication=authentication,
        )
        self.campaign_service = ServiceClient('CampaignManagement', auth, environment='production', version=10)
        self.bulk_service = ServiceClient('Bulk', auth, environment='production', version=10)
        self.bulk_service_manager = BulkServiceManager(auth, environment='production')

    @property
    def campaign_service(self):
        return self._campaign_service

    @campaign_service.setter
    def campaign_service(self, value):
        self._campaign_service = value

    @property
    def reporting_service(self):
        return self._reporting_service

    @reporting_service.setter
    def reporting_service(self, value):
        self._reporting_service = value

    @property
    def bulk_service(self):
        return self._bulk_service

    @bulk_service.setter
    def bulk_service(self, value):
        self._bulk_service = value

    @property
    def account_info(self):
        return self._account_info

    @account_info.setter
    def account_info(self, value):
        self._account_info = value


