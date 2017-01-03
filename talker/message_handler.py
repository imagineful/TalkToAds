from message_parser import *

class MessageHandler(object):

    @staticmethod
    def handle_message(_message, _context):
        message = _message.lower()
        MessageHandler.handle_common_message(message, _context)

        # handle services message
        prefix_regex_map = BingAdsMatch.PrefixRegexMapping
        regex_array = prefix_regex_map['version1']
        message_segments = MessageParser.parse_message(regex_array, message)
        api_with_arguments = MessageParser.parse_api(message_segments, _context)
        return api_with_arguments

    @staticmethod
    def handle_common_message(_message, _context):
        message = _message.lower()
        return MessageParser.parse_common_message(message, _context)

    @staticmethod
    def handle_response(response, context, api_with_argument):
        # TODO move to other place
        AnswerMapping = {
            'GetCampaignsByAccountId' : ['Fetched {0} campaigns, do you want to list all of them?'.format(len(response.Campaign)), lambda r : MessageHandler.show_all_entities(r.Campaign)]
        }
        return AnswerMapping.get(api_with_argument[0], None)

    @staticmethod
    # TODO move to other place
    def show_all_entities(entities):
        for entity in entities:
            print str(entity)