from message_handler import MessageHandler
from config.config_manager import ConfigManager
from bingadsservice.bing_ads_service_manager import BingAdsService
from bingadsservice.bing_ads_context import BingAdsContext


class Talker(object):
    def __init__(self):
        self._config_manager = None
        self._bing_ads_account_info = None
        self._bing_ads_service = None
        self._adwords_account_info = None
        self._adword_servie = None


    @staticmethod
    def start():
        config_manager = ConfigManager()
        config_manager.load_account_data()

        bing_ads_service = BingAdsService(config_manager.bingads_account_info)
        context = BingAdsContext(config_manager.bingads_account_info)

        #campaigns = bing_ads_service.campaign_service.GetCampaignsByAccountId(config_manager.bingads_account_info.account_id)
        while True:
            input = raw_input('>')
            api_with_arguments = MessageHandler.handle_message(input, context)
            print api_with_arguments[0]
            print api_with_arguments[1]
            response = bing_ads_service.call_service(api_with_arguments[0], api_with_arguments[1])
            # TODO answer handler
            print response


talker = Talker()
talker.start()
