

class BingAdsCache(object):
    # TODO add validation for the cache size, add checking for invalid ids
    def __init__(self):
        self._campaigns_by_id = {}
        self._campaigns_by_name = {}
        self._ad_groups_by_id = {}
        self._ad_groups_by_name = {}
        self._ads_by_id = {}

    def add_campaign_by_id(self, id, campaign):
        self._campaigns_by_id[id] = campaign

    def add_campaign_by_name(self, name, campaign):
        self._campaigns_by_name[name] = campaign

    def add_ad_group_by_id(self, id, ad_group):
        self._ad_groups_by_id[id] = ad_group

    def add_ad_group_by_name(self, name, ad_group):
        self._ad_groups_by_id[name] = ad_group

    def add_ad_by_id(self, id, ad):
        self._ads_by_id[id] = ad

    def get_campaign_by_id(self, id):
        return self._campaigns_by_id.get(id, None)

    def get_campaign_by_name(self, name):
        return self._campaigns_by_name.get(name, None)

    def get_ad_group_by_id(self, id):
        return self._ad_groups_by_id.get(id, None)

    def get_ad_group_by_name(self, name):
        return self._ad_groups_by_name.get(name, None)

    def get_ad_by_id(self, id):
        return self._ads_by_id.get(id, None)

    def clear(self):
        self._campaigns_by_id = {}
        self._campaigns_by_name = {}
        self._ad_groups_by_id = {}
        self._ad_groups_by_name = {}
        self._ads_by_id = {}