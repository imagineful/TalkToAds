from message_handler import MessageHandler
from config.config_manager import ConfigManager
from bingadsservice.bing_ads_service_manager import BingAdsService
from common.context import *

# TODO: Handle greetings. e.g. Hello Bing Ads. then enter bing ads mode, hello adwords, then enter adwords mode
# TODO: Handle goodbye message. Goodbye, End service, then exit the program
# TODO: Add answer handler, to answer the questions, or to return the response in a good way
# TODO: Add help support, e.g. help, then print the basic help information
# TODO: Support batch support, e.g. remove all ads in ad group ABC
# TODO: Format the unit test and functional test
# TODO: Write an elegant readme file
# TODO: Add safe logic, e.g. remove all campaigns, should be execute very cautiously.
# TODO: Support Ad words
# TODO: Support facebook ads


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
        context = Context(config_manager.bingads_account_info)

        #campaigns = bing_ads_service.campaign_service.GetCampaignsByAccountId(config_manager.bingads_account_info.account_id)
        while True:
            input = raw_input('>')
            is_common_message, common_message_response = MessageHandler.handle_common_message(input, context)
            if is_common_message:
                print common_message_response
                if context.service_status == 'Completed':
                    return
                continue
            api_with_arguments = MessageHandler.handle_message(input, context)
            if api_with_arguments is not None:
                #print api_with_arguments[0]
                #print api_with_arguments[1]
                api_response = bing_ads_service.call_service(api_with_arguments[0], api_with_arguments[1])
                response = MessageHandler.handle_response(api_response, context, api_with_arguments)
                if response is not None:
                    print response[0]
                    confirm_input = raw_input('')
                    if confirm_input.lower() == 'yes':
                        response[1](api_response)
                else:
                    print 'Something bad happened...'


talker = Talker()
talker.start()
