from tink_data_to_my.real_exchange import Real_Exchange
from tink_data_to_my.tink_data_to_money import money_value_to_float, quotation_to_float
from tink_data_to_my.trading_status import Security_Trading_Status


class Bond:

    def __init__(self, figi, quantity, expected_yield, nkd_aci, current_price, quantity_lots, ticker, class_code, isin,
                 lot, currency, name, exchange, coupon_quantity_per_year, maturity_date, nominal, state_reg_date,
                 placement_date, placement_price, country_of_risk, country_of_risk_name, sector, issue_kind, issue_size,
                 issue_size_plan, trading_status, otc_flag, buy_available_flag, sell_available_flag,
                 floating_coupon_flag, perpetual_flag, amortization_flag, min_price_increment, api_trade_available_flag,
                 uid, real_exchange):
        self.figi = figi
        self.type = 'bond'
        self.quantity = quotation_to_float(quantity)
        self.current_profitability = quotation_to_float(expected_yield)
        self.nkd_aci = money_value_to_float(nkd_aci)
        self.current_price = money_value_to_float(current_price)
        self.quantity_lots = quotation_to_float(quantity_lots)
        self.ticker = ticker
        self.class_code = class_code
        self.isin = isin
        self.lot = lot
        self.currency = currency
        self.name = name
        self.exchange = exchange
        self.coupon_quantity_per_year = coupon_quantity_per_year
        self.maturity_date = maturity_date.strftime("%d.%m.%Y %H:%M:%S")
        self.nominal = money_value_to_float(nominal)
        self.state_reg_date = state_reg_date.strftime("%d.%m.%Y %H:%M:%S")
        self.placement_date = placement_date.strftime("%d.%m.%Y %H:%M:%S")
        self.placement_price = money_value_to_float(placement_price)
        self.country_of_risk = country_of_risk
        self.country_of_risk_name = country_of_risk_name
        self.sector = sector
        self.issue_kind = issue_kind
        self.issue_size = issue_size
        self.issue_size_plan = issue_size_plan
        self.trading_status = Security_Trading_Status[trading_status.value]
        self.otc_flag = otc_flag
        self.buy_available_flag = buy_available_flag
        self.sell_available_flag = sell_available_flag
        self.floating_coupon_flag = floating_coupon_flag
        self.perpetual_flag = perpetual_flag
        self.amortization_flag = amortization_flag
        self.min_price_increment = quotation_to_float(min_price_increment)
        self.api_trade_available_flag = api_trade_available_flag
        self.uid = uid
        self.real_exchange = Real_Exchange[real_exchange.value]

    def __str__(self):
        return f"{self.type}: навание облигации '{self.name}', число данных облигаций = {str(self.quantity)}, нкд = {str(self.nkd_aci)}, " \
               f"текущая цена за одну облигацию = {str(self.current_price)}, лот состоит из {str(self.lot)} облигаций, " \
               f"у вас есть уже {str(self.quantity_lots)} лотов, стоимость всех данных облигаций = {str(self.current_price * self.quantity)}, " \
               f"валюта расчётов - {self.currency}, торговая площадка '{self.exchange}', в год {str(self.coupon_quantity_per_year)} купонов, " \
               f"дата погашения - {self.maturity_date}, номинал облигации - {str(self.nominal)}, основаная страна бизнеса - {self.country_of_risk_name}, " \
               f"сектор экономики - {self.sector}, текущий режим торгов облигацией - {self.trading_status[1]}, уникальный идентификатор - {self.uid}, " \
               f"реальная площадка торгов - {self.real_exchange[1]}."
