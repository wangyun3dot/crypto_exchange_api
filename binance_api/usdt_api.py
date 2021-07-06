from .client import Client
from .consts import *

# 对应binance u本位合约交易
class USDTAPI(Client):

    def __init__(self, api_key=None, api_secret=None, requests_params=None):
        Client.__init__(self, api_key, api_secret, requests_params)
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.session = self._init_session()
        self._requests_params = requests_params
        self.response = None
        # 添加base_url
        self.base_url = USDT_CONTRACT_URL
    
    ################### 行情接口 ###################
    # 以market + (method) + 接口为名字
    # 测试服务器联通性
    def market_get_ping(self):
        return self._request_api("get", "/fapi/v1/ping")
    
    def market_get_exchangeInfo(self):
        return self._request_api("get", "/fapi/v1/exchangeInfo")
    

    ################### 账户和交易接口 ###################
    # 以trade+ (method) + 接口为名字
    # 划转
    # 获取划转历史
    def trade_get_allorders(self, symbol, orderId='', startTime='', endTime=''):
        params = {}
        params['symbol'] = symbol
        if orderId:
            params['orderId'] = orderId
        if startTime:
            params['startTime'] = startTime
        if endTime:
            params['endTime'] = endTime
        params['limit'] = 1000
        return self._request_api("get", "/fapi/v1/allOrders", True, data=params)

    # 更改持仓模式
    # 查询持仓模式
    def trade_get_positionSide(self):
        params = {}
        return self._request_api("get", "/fapi/v1/positionSide/dual", True, data=params)

    # ...
    # 账户余额V2 weight 5
    def trade_get_balance(self):
        params = {}
        return self._request_api("get", "/fapi/v2/balance", True, data=params)

    # 账户信息V2  (持仓的情况在这里！！！) weight 5
    def trade_get_account(self):
        params = {}
        return self._request_api("get", "/fapi/v2/account", True, data=params)

    # 用户持仓风险  (持仓的情况在这里！！！) weight 5 
    def trade_get_positionRisk(self, symbol=None):
        params = {}
        if symbol:
            params["symbol"] =symbol
        return self._request_api("get", "/fapi/v2/positionRisk", True, data=params)
    
    # 获取账户损益资金流水 weight 30
    def trade_get_income(self, symbol=None, incomeType=None, startTime=None, endTime=None, limit=1000, ):
        params = {}
        if symbol:
            params["symbol"] = symbol
        if incomeType:
            params["incomeType"] = incomeType
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if limit:
            params["limit"] = limit
        return self._request_api("get", "/fapi/v1/income", True, data=params)
        
