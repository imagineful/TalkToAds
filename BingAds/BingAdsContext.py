from Common.Context import Context


class BingAdsContext(Context):
    def __init__(self, account):
        super(BingAdsContext, self).__init__(account)
        self._ads_platform = 'bingads'
