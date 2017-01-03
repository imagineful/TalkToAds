from bingadsservice.bing_ads_cache import BingAdsCache
class Context(object):
    def __init__(self, account):
        self._account = account
        self._campaign = None
        self._ad_group = None
        self._current_entity = None
        self._ads_platform = None
        self._cache = BingAdsCache()
        self._service_status = 'Active'

    @property
    def ads_platform(self):
        return self._ads_platform

    @ads_platform.setter
    def ads_platform(self, value):
        self._ads_platform = value

    @property
    def account(self):
        """
        BingAdsAccountInfo object
        AdWordsAccountInfo object
        :return:
        """
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def campaign(self):
        return self._campaign

    @campaign.setter
    def campaign(self, value):
        self._campaign = value

    @property
    def ad_group(self):
        return self._ad_group

    @ad_group.setter
    def ad_group(self, value):
        self._ad_group = value

    @property
    def current_entity(self):
        return self._current_entity

    @current_entity.setter
    def current_entity(self, value):
        self._current_entity = value

    @property
    def cache(self):
        return self._cache

    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value

    def clear(self):
        self._account = None
        self._campaign = None
        self._ad_group = None
        self._current_entity = None
        self._ads_platform = None

    def clear_cache(self):
        self._cache.clear()
