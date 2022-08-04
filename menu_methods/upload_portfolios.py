from tinkoff.invest import Client, InstrumentIdType

from classes.all_portfolios import All_Portfolios
from classes.bond import Bond
from classes.currency import Currency
from classes.etf import ETF
from classes.portfolio import Portfolio
from classes.stock import Stock


def upload_portfolios(client, number: int = -1) -> All_Portfolios:
    accounts = client.users.get_accounts().accounts
    all_portfolios = All_Portfolios()
    account_num = 1
    for account in accounts:
        if number == -1 or number == len(accounts) + 1 or account_num == number:
            portfolio_all = client.operations.get_portfolio(account_id=account.id)
            new_portfolio = Portfolio(account.id, account.type, account.name, account.status, account.opened_date,
                                      account.access_level, portfolio_all.total_amount_shares,
                                      portfolio_all.total_amount_bonds, portfolio_all.total_amount_etf,
                                      portfolio_all.total_amount_currencies, portfolio_all.total_amount_futures)
            portfolios = client.operations.get_portfolio(account_id=account.id).positions
            for portfolio in portfolios:
                if portfolio.instrument_type == 'share':
                    instr_share = client.instruments.share_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=portfolio.figi).instrument
                    new_portfolio.add_stock(Stock(portfolio.figi, portfolio.quantity, portfolio.expected_yield,
                                                  portfolio.current_price, portfolio.quantity_lots, instr_share.ticker,
                                                  instr_share.class_code, instr_share.isin, instr_share.lot,
                                                  instr_share.currency, instr_share.name, instr_share.exchange, instr_share.ipo_date,
                                                  instr_share.issue_size, instr_share.issue_size_plan, instr_share.country_of_risk,
                                                  instr_share.country_of_risk_name, instr_share.sector, instr_share.nominal,
                                                  instr_share.trading_status, instr_share.otc_flag, instr_share.buy_available_flag,
                                                  instr_share.sell_available_flag, instr_share.div_yield_flag,
                                                  instr_share.share_type, instr_share.min_price_increment, instr_share.api_trade_available_flag,
                                                  instr_share.uid, instr_share.real_exchange, instr_share.position_uid))
                elif portfolio.instrument_type == 'bond':
                    instr_bond = client.instruments.bond_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=portfolio.figi).instrument
                    new_portfolio.add_bond(Bond(portfolio.figi, portfolio.quantity, portfolio.expected_yield,
                                                instr_bond.aci_value, portfolio.current_price, portfolio.quantity_lots,
                                                instr_bond.ticker, instr_bond.class_code, instr_bond.isin, instr_bond.lot,
                                                instr_bond.currency, instr_bond.name, instr_bond.exchange, instr_bond.coupon_quantity_per_year,
                                                instr_bond.maturity_date, instr_bond.nominal, instr_bond.state_reg_date,
                                                instr_bond.placement_date, instr_bond.placement_price,
                                                instr_bond.country_of_risk, instr_bond.country_of_risk_name, instr_bond.sector,
                                                instr_bond.issue_kind, instr_bond.issue_size, instr_bond.issue_size_plan,
                                                instr_bond.trading_status, instr_bond.otc_flag, instr_bond.buy_available_flag,
                                                instr_bond.sell_available_flag, instr_bond.floating_coupon_flag, instr_bond.perpetual_flag,
                                                instr_bond.amortization_flag, instr_bond.min_price_increment, instr_bond.api_trade_available_flag,
                                                instr_bond.uid, instr_bond.real_exchange))
                elif portfolio.instrument_type == 'etf':
                    instr_etf = client.instruments.etf_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=portfolio.figi).instrument
                    new_portfolio.add_etf(ETF(portfolio.figi, portfolio.quantity, portfolio.expected_yield,
                                              portfolio.current_price, portfolio.quantity_lots, instr_etf.ticker,
                                              instr_etf.class_code, instr_etf.isin, instr_etf.lot, instr_etf.currency,
                                              instr_etf.name, instr_etf.exchange, instr_etf.fixed_commission, instr_etf.focus_type,
                                              instr_etf.released_date, instr_etf.num_shares, instr_etf.country_of_risk,
                                              instr_etf.country_of_risk_name, instr_etf.sector, instr_etf.rebalancing_freq,
                                              instr_etf.trading_status, instr_etf.otc_flag, instr_etf.buy_available_flag,
                                              instr_etf.sell_available_flag, instr_etf.min_price_increment, instr_etf.api_trade_available_flag,
                                              instr_etf.uid, instr_etf.real_exchange, instr_etf.position_uid))
                elif portfolio.instrument_type == 'currency':
                    instr_currency = client.instruments.currency_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=portfolio.figi).instrument
                    new_portfolio.add_currency(Currency(portfolio.figi, portfolio.quantity, portfolio.expected_yield,
                                                        portfolio.current_price, portfolio.quantity_lots, instr_currency.ticker,
                                                        instr_currency.class_code, instr_currency.isin, instr_currency.lot,
                                                        instr_currency.currency, instr_currency.name, instr_currency.exchange,
                                                        instr_currency.nominal, instr_currency.country_of_risk,
                                                        instr_currency.country_of_risk_name, instr_currency.trading_status,
                                                        instr_currency.otc_flag, instr_currency.buy_available_flag,
                                                        instr_currency.sell_available_flag, instr_currency.iso_currency_name,
                                                        instr_currency.min_price_increment, instr_currency.api_trade_available_flag,
                                                        instr_currency.uid, instr_currency.real_exchange, instr_currency.position_uid))
                else:
                    raise Exception(f"I don't now {portfolio.instrument_type}")
            all_portfolios.add_portfolio(new_portfolio)
        account_num += 1
    return all_portfolios
