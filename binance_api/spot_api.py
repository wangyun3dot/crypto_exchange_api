from .client import Client
from .consts import *

class SpotAPI(Client):

    def __init__(self, api_key=None, api_secret=None, requests_params=None):
        Client.__init__(self, api_key, api_secret, requests_params)
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.session = self._init_session()
        self._requests_params = requests_params
        self.response = None
        # 添加base_url
        self.base_url = SPOT_URL
    
    ################### 钱包接口 ###################
    # 系统状态
    def wallet_get_systemStatus(self):
        return self._request_api("get", "/wapi/v3/systemStatus.html")
    # 获取所有币信息
    def wallet_get_config(self):
        return self._request_api("get", "/sapi/v1/capital/config/getall")
    # 查询每日资产快照
    def wallet_get_accountSnapshot(self, accountType="SPOT"):
        params = {
            "type": accountType,
        }
        return self._request_api("get", "/sapi/v1/accountSnapshot", True, data=params)
    # 关闭站内划转
    # 开启站内划转
    # 提币SAPI
    # 提币
    # 获取充值历史
    # 获取提币历史
    # 获取充值地址
    # 账户状态
    # 账户API交易状态
    # 小额资产转换BNB历史
    # 小额资产转换
    # 资产利息记录
    # 上架资产详情
    # 交易手续费率查询
    # 用户万向划转
    # 查询用户万向划转历史
    ################### 子母账户接口 ###################

    ################### 行情接口 ###################
    # 最新价格
    def market_ticker(self, symbol=None):
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._request_api("get", "/api/v3/ticker/price")

    ################### 现货账户和交易接口 ###################
    # 账户信息 weight 10
    def spot_get_account(self):
        params = {}
        return self._request_api("get", "/api/v3/account", True, data=params)

    ################### 杠杆账户和交易接口 ###################

    # 查询全仓杠杆账户详情 weight 1
    def level_get_account(self):
        params = {}
        return self._request_api("get", "/sapi/v1/margin/account", True, data=params)
    
    # 查询杠杆逐仓账户信息 weight 1
    def level_get_isolated_account(self, symbols=None):
        params = {}
        if symbols:
            params["symbols"] = symbols
        return self._request_api("get", "/sapi/v1/margin/isolated/account", True, data=params)

    # 获取利息历史
    def level_get_interest_history(self, 
        asset=None,
        isolatedSymbol=None,
        startTime=None,
        endTime=None,
        current=None,
        size=None,
        archived=False,
        ):
        params = {}
        if asset:
            params["asset"] = asset
        if isolatedSymbol:
            params["isolatedSymbol"] = isolatedSymbol
        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime
        if current:
            params["current"] = current
        if size:
            params["size"] = size
        if archived:
            params["archived"] = archived
        return self._request_api("get", "/sapi/v1/margin/interestHistory", True, data=params)


    ################### 币安宝接口 ###################

    ################### 矿池接口 ###################

    ################### 合约接口 ###################

    ################### 杠杆代币接口 ###################

    ################### 币安挖矿接口 ###################
    