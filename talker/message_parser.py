import re
from bingadsservice.bing_ads_call_format import *

class MessageParser:
    @staticmethod
    def parse_message(match_list, message):
        """
        parse the message to arguments list
        :param match_list: regex list that used to parse the message
        :param message: input message
        :return: list of argument
        """
        result = []
        current_message = message
        for regex in match_list:
            match = re.search(regex, current_message)
            if match:
                arg = MessageProcessHelper.process_words(match.group(1))
                result.append(arg)
                span = match.span(1)
                current_message = current_message[span[1]:]
            else:
                break
        return result

    @staticmethod
    def parse_api(arguments, context):
        """
        parse the argument list to the target API name and the argument api requires
        :param arguments: argument list
        :param context: Ads service context
        :return:
        """
        if len(arguments) < 2:
            return None
        if len(arguments) == 2:
            arguments.append('')

        api_mapping_key = (arguments[0], arguments[1], arguments[2])
        if api_mapping_key not in BingAdsAPIMapping.keys():
            return None
        api_name = BingAdsAPIMapping[api_mapping_key]
        arg_list = []
        if len(arguments) > 3:
            arg_list.extend(arguments[3:])

        # the arg list need to convert to the api required format
        api_arg_list = MessageProcessHelper.process_arg_list(api_name, arg_list, context)

        return [api_name, api_arg_list]


class MessageProcessHelper:
    WordsMappings = {
        'howmany' : 'get',
        'count'  : 'get',
        'create' : 'add',
        'remove' : 'delete'
    }

    @staticmethod
    def process_words(word):
        word = word.replace(' ', '').rstrip('s')  # TODO confirm no special case that entity ends with s

        if word in MessageProcessHelper.WordsMappings.keys():
            return MessageProcessHelper.WordsMappings[word]
        return word

    @staticmethod
    def process_arg_list(api_name, arg_list, context):
        ApiArgumentMapping = {
            'GetCampaignsByAccountId': context.account.account_id
        }
        api_arg_list = []
        if api_name in ApiArgumentMapping.keys():
            api_arg_list.append(ApiArgumentMapping[api_name])

        return api_arg_list


