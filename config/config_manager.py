import os
from ConfigParser import SafeConfigParser
from bingadsservice.bing_ads_account_info import *

current_path = os.path.dirname(os.path.realpath(__file__))

class ConfigManager:
    def __init__(self):
        self._bing_ads_account_info = BingAdsAccountInfo()
        self._ad_words_account_info = None

    def load_account_data(self):
        account_data_path_file = '{0}/account_data_path.conf'.format(current_path)
        config_parser = SafeConfigParser()

        config_parser.read(account_data_path_file)
        config_data_path = config_parser.get('Path', 'account_data_path')

        # now parse the account data
        config_parser.read(config_data_path)
        self._bing_ads_account_info.account_id = int(config_parser.get('BingAds', 'account_id'))
        self._bing_ads_account_info.customer_id = int(config_parser.get('BingAds', 'customer_id'))
        self._bing_ads_account_info.client_id = config_parser.get('BingAds', 'client_id')
        self._bing_ads_account_info.access_token = config_parser.get('BingAds', 'access_token')
        self._bing_ads_account_info.refresh_token = config_parser.get('BingAds', 'refresh_token')
        self._bing_ads_account_info.developer_token = config_parser.get('BingAds', 'developer_token')

        # TODO parse adwordsservice

    @property
    def bingads_account_info(self):
        return self._bing_ads_account_info

    @property
    def ad_words_account_info(self):
        return self._ad_words_account_info
