from tink_data_to_my.focus_type import Focus_Type
from tink_data_to_my.real_exchange import Real_Exchange
from tink_data_to_my.tink_data_to_money import quotation_to_float, money_value_to_float
from tink_data_to_my.trading_status import Security_Trading_Status


class ETF:

    def __init__(self, figi, quantity, expected_yield, current_price, quantity_lots, ticker, class_code, isin, lot,
                 currency, name, exchange, fixed_commission, focus_type, released_date, num_shares, country_of_risk,
                 country_of_risk_name, sector, rebalancing_freq, trading_status, otc_flag, buy_available_flag,
                 sell_available_flag, min_price_increment, api_trade_available_flag, uid, real_exchange, position_uid):
        self.figi = figi
        self.type = 'etf'
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
        self.fixed_commission = quotation_to_float(fixed_commission)
        self.focus_type = Focus_Type[focus_type]
        self.released_date = released_date.strftime("%d.%m.%Y %H:%M:%S")
        self.num_shares = quotation_to_float(num_shares)
        self.country_of_risk = country_of_risk
        self.country_of_risk_name = country_of_risk_name
        self.sector = sector
        self.rebalancing_freq = rebalancing_freq
        self.trading_status = Security_Trading_Status[trading_status.value]
        self.otc_flag = otc_flag
        self.buy_available_flag = buy_available_flag
        self.sell_available_flag = sell_available_flag
        self.min_price_increment = quotation_to_float(min_price_increment)
        self.api_trade_available_flag = api_trade_available_flag
        self.uid = uid
        self.real_exchange = Real_Exchange[real_exchange.value]
        self.position_uid = position_uid

    def __str__(self):

        return f"{self.type}: навание фонда '{self.name}', число данных бумаг фонда = {str(self.quantity)}, " \
               f"текущая цена за одну бумагу фонда = {str(self.current_price)}, лот состоит из {str(self.lot)} бумаг фонда, " \
               f"у вас есть уже {str(self.quantity_lots)} лотов, стоимость всех данных бумаг фонда = {str(self.current_price * self.quantity)}, " \
               f"валюта расчётов - {self.currency}, торговая площадка '{self.exchange}', размер фиксированной коммисии фонда - {self.fixed_commission}, " \
               f"направление фонда - {self.focus_type}, дата выпуска - {self.released_date}, основаная страна бизнеса - {self.country_of_risk_name}, " \
               f"сектор экономики - {self.sector}, текущий режим торгов бумагами фонда - {self.trading_status[1]}, уникальный идентификатор - {self.uid}, " \
               f"реальная площадка торгов - {self.real_exchange[1]}, количество бумаг фонда в обращении - {self.num_shares}, " \
               f"частота ребалансировки - {self.rebalancing_freq}, уникальный идентификатор позиции - {self.position_uid}."
