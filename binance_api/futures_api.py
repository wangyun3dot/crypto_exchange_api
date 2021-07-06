import os

os.sys.path.append("..")
from .client import Client
from .consts import *

# 对应binance 币本位合约交易
class FuturesAPI(Client):

    def __init__(self, api_key=None, api_secret=None, requests_params=None):
        Client.__init__(self, api_key, api_secret, requests_params)
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.session = self._init_session()
        self._requests_params = requests_params
        self.response = None
        # 添加base_url
        self.base_url = FUTURES_COIN_URL

    ################### 行情接口 ###################
    # 以market + (method) + 接口为名字
    # 测试服务器联通性
    def market_get_ping(self):
        return self._request_api("get", "/dapi/v1/ping")
    

    ################### 账户和交易接口 ###################
    # 以trade+ (method) + 接口为名字
    # 划转
    # 获取划转历史
    # 更改持仓模式
    # 查询持仓模式
    def trade_get_positionSide(self):
        params = {}
        return self._request_api("get", "/dapi/v1/positionSide/dual", True, data=params)

    # ...
    # 账户余额(USER_DATA)
    def trade_get_balance(self):
        params = {}
        return self._request_api("get", "/dapi/v1/balance", True, data=params)

    # 账户信息(USER_DATA)  weight 5
    def trade_get_account(self):
        params = {}
        return self._request_api("get", "/dapi/v1/account", True, data=params)
    
    # 用户持仓风险  (持仓的情况在这里！！！) weight 1
    def trade_get_positionRisk(self, symbol=None):
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._request_api("get", "/dapi/v1/positionRisk", True, data=params)
