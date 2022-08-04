from tink_data_to_my.real_exchange import Real_Exchange
from tink_data_to_my.share_type import Share_Type
from tink_data_to_my.tink_data_to_money import quotation_to_float, money_value_to_float
from tink_data_to_my.trading_status import Security_Trading_Status


class Stock:

    def __init__(self, figi, quantity, expected_yield, current_price, quantity_lots, ticker, class_code, isin, lot,
                 currency, name, exchange, ipo_date, issue_size, issue_size_plan, country_of_risk, country_of_risk_name,
                 sector, nominal, trading_status, otc_flag, buy_available_flag, sell_available_flag, div_yield_flag,
                 share_type, min_price_increment, api_trade_available_flag, uid, real_exchange, position_uid):
        self.figi = figi
        self.type = 'stock'
        self.quantity = quotation_to_float(quantity)
        self.current_profitability = quotation_to_float(expected_yield)
        self.current_price = money_value_to_float(current_price)
        self.quantity_lots = quotation_to_float(quantity_lots)
        self.ticker = ticker
        self.class_code = class_code
        self.isin = isin
        self.lot = lot
        self.currency = currency
        self.name = name
        self.exchange = exchange
        self.ipo_date = ipo_date.strftime("%d.%m.%Y %H:%M:%S")
        self.issue_size = issue_size
        self.issue_size_plan = issue_size_plan
        self.country_of_risk = country_of_risk
        self.country_of_risk_name = country_of_risk_name
        self.sector = sector
        self.nominal = money_value_to_float(nominal)
        self.trading_status = Security_Trading_Status[trading_status.value]
        self.otc_flag = otc_flag
        self.buy_available_flag = buy_available_flag
        self.sell_available_flag = sell_available_flag
        self.div_yield_flag = div_yield_flag
        self.share_type = Share_Type[share_type.value]
        self.min_price_increment = quotation_to_float(min_price_increment)
        self.api_trade_available_flag = api_trade_available_flag
        self.uid = uid
        self.real_exchange = Real_Exchange[real_exchange.value]
        self.position_uid = position_uid

    def __str__(self):
        return f"{self.type}: навание акции '{self.name}', число данных акций = {str(self.quantity)}, " \
               f"текущая цена за одну акцию = {str(self.current_price)}, лот состоит из {str(self.lot)} акций, " \
               f"у вас есть уже {str(self.quantity_lots)} лотов, стоимость всех данных акций = {str(self.current_price * self.quantity)}, " \
               f"валюта расчётов - {self.currency}, торговая площадка '{self.exchange}', есть ли дивиденты {self.div_yield_flag}, " \
               f"дата ipo - {self.ipo_date}, номинал акции - {str(self.nominal)}, основаная страна бизнеса - {self.country_of_risk_name}, " \
               f"сектор экономики - {self.sector}, текущий режим торгов акцией - {self.trading_status[1]}, уникальный идентификатор - {self.uid}, " \
               f"реальная площадка торгов - {self.real_exchange[1]}, тип акции - {self.share_type[1]}, уникальный идентификатор позиции - {self.position_uid}."
