import datetime

from tinkoff.invest import InstrumentIdType

from classes.bond import Bond
from classes.currency import Currency
from classes.etf import ETF
from classes.operation import Operation
from classes.stock import Stock
from classes.price_paper import PricePaper
from terminal_color import fg, bg
from tink_data_to_my.account_level import Account_Level
from tink_data_to_my.account_status import Account_Status
from tink_data_to_my.account_type import Account_Type
from tink_data_to_my.tink_data_to_money import money_value_to_float


class Portfolio:

    def __init__(self, portfolio_id: str, account_type, name: str, status, opened_date, access_level, total_amount_shares,
                 total_amount_bonds, total_amount_etf, total_amount_currencies, total_amount_futures):
        self.portfolio_id = portfolio_id
        self.account_type = Account_Type[account_type.value]
        self.name = name
        self.status = Account_Status[status.value]
        self.opened_date = opened_date.strftime("%d.%m.%Y %H:%M:%S")
        self.access_level = Account_Level[access_level.value]
        self.type = 'portfolio'
        self.__Bonds = []
        self.__Stocks = []
        self.__ETFs = []
        self.__Currencies = []
        self.__Operations = []
        self.time_paper = {}
        self.total_amount_shares = money_value_to_float(total_amount_shares)
        self.total_amount_bonds = money_value_to_float(total_amount_bonds)
        self.total_amount_etfs = money_value_to_float(total_amount_etf)
        self.total_amount_currencies = money_value_to_float(total_amount_currencies)
        self.total_amount_futures = money_value_to_float(total_amount_futures)

    def __str__(self):
        return self.self_info() + "\n" + self.return_stocks() + "\n" + self.return_bonds() + "\n" + \
               self.return_etfs() + "\n" + self.return_currencies()

    def total_amount(self) -> PricePaper:
        return self.total_amount_futures + self.total_amount_currencies + self.total_amount_etfs + \
               self.total_amount_shares + self.total_amount_bonds

    def show_total_amount_everyone(self) -> None:
        self.show_self()
        print(f'Общая стоимость - {self.total_amount()}')
        print(f'Стоимость акций - {self.total_amount_shares}')
        print(f'Стоимость облигаций - {self.total_amount_bonds}')
        print(f'Стоимость фондов - {self.total_amount_etfs}')
        print(f'Стоимость фьючесов - {self.total_amount_futures}')
        print(f'Стоимость всех валют - {self.total_amount_currencies}')

    def self_info(self) -> str:
        return fg.orange + fg.bold + fg.underline + bg.black + "Название счёта - \"" + self.name + "\", его id = " + \
               self.portfolio_id + ", число акций = " + str(self.count_stocks()) + ", число облигаций = " + \
               str(self.count_bonds()) + ", число фондов = " + str(self.count_etfs()) + ", число валют = " + \
               str(self.count_currencies()) + ", общая стоимость = " + str(self.total_amount()) + ", тип аккаунта - " +\
               self.account_type[1] + ", стату аккаунта - " + self.status[1] + ", уровень аккаунта - " +\
               self.access_level[1] + fg.end

    def show_self(self) -> None:
        print(self.self_info())

    def get_opened_date(self):
        date = self.opened_date.split('.')
        return datetime.datetime(int(date[2][:4]), int(date[1]), int(date[0]))

    def add_stock(self, stock: Stock):
        if stock.type == 'stock':
            self.__Stocks.append(stock)
        else:
            raise Exception(f'{str(stock)} is not a Stock')

    def show_stocks(self) -> None:
        for item in self.__Stocks:
            print(fg.red + bg.black + str(item) + fg.end)

    def return_stocks(self) -> str:
        return fg.red + bg.black + "\n".join([str(i) for i in self.__Stocks]) + fg.end

    def count_stocks(self) -> int:
        return len(self.__Stocks)

    def add_bond(self, bond: Bond):
        if bond.type == 'bond':
            self.__Bonds.append(bond)
        else:
            raise Exception(f'{str(bond)} is not a Bond')

    def show_bonds(self) -> None:
        for item in self.__Bonds:
            print(fg.green + bg.black + str(item) + fg.end)

    def return_bonds(self) -> str:
        return fg.green + bg.black + "\n".join([str(i) for i in self.__Bonds]) + fg.end

    def count_bonds(self) -> int:
        return len(self.__Bonds)

    def add_etf(self, etf: ETF):
        if etf.type == 'etf':
            self.__ETFs.append(etf)
        else:
            raise Exception(f'{str(etf)} is not an ETF')

    def show_etfs(self) -> None:
        for item in self.__ETFs:
            print(fg.lightcyan + bg.black + str(item) + fg.end)

    def return_etfs(self) -> str:
        return fg.lightcyan + bg.black + "\n".join([str(i) for i in self.__ETFs]) + fg.end

    def count_etfs(self) -> int:
        return len(self.__ETFs)

    def add_currency(self, currency: Currency):
        if currency.type == 'currency':
            self.__Currencies.append(currency)
        else:
            raise Exception(f'{str(currency)} is not a Currency')

    def show_currencies(self) -> None:
        for item in self.__Currencies:
            print(fg.blue + bg.black + str(item) + fg.end)

    def return_currencies(self) -> str:
        return fg.blue + bg.black + "\n".join([str(i) for i in self.__Currencies]) + fg.end

    def count_currencies(self) -> int:
        return len(self.__Currencies)

    def add_operation(self, operation: Operation):
        if operation.type == 'operation':
            self.__Operations.append(operation)
            if operation.figi in self.time_paper:
                self.time_paper[operation.figi].append(operation)
            else:
                self.time_paper[operation.figi] = [operation]
        else:
            raise Exception(f'{str(operation)} is not a Operation')

    def show_operations(self, count) -> None:
        if count > 0:
            self.show_self()
            num = 0
            for item in self.__Operations:
                print(fg.yellow + bg.black + str(item) + fg.end)
                num += 1
                if count <= num:
                    break

    def return_operations(self) -> str:
        return fg.yellow + bg.black + "\n".join([str(i) for i in self.__Operations]) + fg.end

    def count_operations(self) -> int:
        return len(self.__Operations)

    def get_time_paper(self) -> dict:
        return self.time_paper

    def show_time_paper(self, client):
        for figi, operations in self.time_paper.items():
            instr = None
            if operations[0].instrument_type == 'share':
                instr = client.instruments.share_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                    id=figi).instrument
            elif operations[0].instrument_type == 'bond':
                instr = client.instruments.bond_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                   id=figi).instrument
            elif operations[0].instrument_type == 'etf':
                instr = client.instruments.etf_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                  id=figi).instrument
            elif operations[0].instrument_type == 'currency':
                instr = client.instruments.currency_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI,
                                                       id=figi).instrument
            if instr is None:
                print('Пополнение брокерского счёта')
            else:
                print(f"{operations[0].instrument_type} '{instr.name}' : ")
            data = {}
            for operation in operations:
                print("  ", operation)
                if operation.operation_type in data:
                    # print(operation)
                    if operation.currency in data[operation.operation_type]:
                        data[operation.operation_type][operation.currency] += operation.payment
                    else:
                        data[operation.operation_type][operation.currency] = operation.payment
                else:
                    data[operation.operation_type] = {}
                    data[operation.operation_type][operation.currency] = operation.payment
            print("    result: ", end="")
            for data_key, data_value in data.items():
                print(f"'{data_key[1]}' {', '.join(str(round(x, 5)) for x in data_value.values())}; ", end="")
            print()
