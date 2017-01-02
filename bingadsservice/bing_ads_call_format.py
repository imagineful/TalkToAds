class BingAdsCallFormat(object):
    def __init__(self):
        self._method_name = None
        self._parameters = None
        self._operation = None
        self._entity = None
        self._bywhat = None

    @property
    def method_name(self):
        return self._method_name

    @method_name.setter
    def method_name(self, value):
        self._method_name = value

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        self._entity = value

    @property
    def bywhat(self):
        return self._bywhat

    @bywhat.setter
    def bywhat(self, value):
        self._bywhat = value

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        self._parameters = value


class BingAdsAPIOperator:
    Get = 'Get'
    Add = 'Add'
    Update = 'Update'
    Set = 'Set'
    Delete = 'Delete'


class BingAdsMatch:
    Prefix = ['i want to', 'please', "i'd like to", 'i would like to']
    Get = ['get', 'fetch', 'how many']
    Entity = ['campaign', 'ad group', 'adgroup', 'ad', 'keyword']
    ByWhat = ['in id', 'in campaign', 'in ad group', 'in adgroup']

    PrefixRegexMapping = {
        'version1': ['(how many|get|fetch|count|check|add|create|update|change|delete|remove).*',  '(campaigns*|ad *groups*).*', '.*in.*(account|campaign|ad *group).*', ' *([\d\w ]*)'],
        #'how many' : 'how many (campaigns*|ad *groups*) .*in.*(account|campaign|ad *group) *(.*)'
    }

BingAdsAPIMapping = {
    # TODO change value to a list e.g. ['API', GetCampaignsByAccountId], ['Error', 'you must specify your campaign id']
    ('get', 'campaign', 'account') :    'GetCampaignsByAccountId',
    ('get', 'campaign', '') :           'GetCampaignsByAccountId',
    ('get', 'campaign', 'id') :         'GetCampaignsByIds',
    ('get', 'adgroup', 'campaign') :    'GetAdGroupByCampaignId',
    ('get', 'adgroup', 'id'):           'GetAdGroupByIds',
    ('get', 'adgroup', ''):           'TODO support multi api calls',
    ('get', 'adgroup', 'account'):    'TODO support multi api calls',
    ('get', 'remarketinglist', ''):     'GetRemarketingList',
    ('get', 'remarketinglist', 'account'): 'GetRemarketingList',
}
