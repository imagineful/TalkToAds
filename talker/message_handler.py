from bingadsservice.bing_ads_call_format import *
from message_parser import *
import re

class MessageHandler(object):

    @staticmethod
    def handle_message(_message, _context):
        message = _message.lower()
        # TODO pre process message, e.g. remove spaces, remove 'Hi', 'Hello', 'Please'
        prefix_regex_map = BingAdsMatch.PrefixRegexMapping
        regex_array = prefix_regex_map['version1']
        message_segments = MessageParser.parse_message(regex_array, message)
        api_with_arguments = MessageParser.parse_api(message_segments, _context)
        return api_with_arguments


