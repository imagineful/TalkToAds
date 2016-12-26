
import sys
from MessageHandler import MessageHandler
from Config.ConfigManager import ConfigManager
from BingAds.BingAdsServiceManager import BingAdsService


class Talker(object):
    @staticmethod
    def start():
        config_manager = ConfigManager()
        config_manager.load_account_data()

        bing_ads_service = BingAdsService(config_manager.bingads_account_info)


        campaigns = bing_ads_service.campaign_service.GetCampaignsByAccountId(config_manager.bingads_account_info.account_id)
        while True:
            input = raw_input('>>>')
            handle_result = MessageHandler.handle_message(input)


talker = Talker()
talker.start()
