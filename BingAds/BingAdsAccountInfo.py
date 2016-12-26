class BingAdsAccountInfo(object):
    def __init__(self):
        self._account_id = None
        self._customer_id = None
        self._client_id = None
        self._access_token = None
        self._refresh_token = None
        self._developer_token = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    @property
    def developer_token(self):
        return self._developer_token

    @developer_token.setter
    def developer_token(self, value):
        self._developer_token = value
