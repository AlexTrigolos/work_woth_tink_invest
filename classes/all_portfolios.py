from classes.portfolio import Portfolio
from iterators.all_portfolios_iter import All_Portfolios_Iterator


class All_Portfolios:

    def __init__(self):
        self.__Portfolios = []

    def __index__(self):
        pass

    def __getitem__(self, item):
        index = 0
        for portfolio in self.__Portfolios:
            if index == item:
                return portfolio
            index += 1

    def __str__(self):
        return "\n".join([str(i) for i in self.__Portfolios])

    def __iter__(self):
        return All_Portfolios_Iterator(self)

    def __len__(self):
        return len(self.__Portfolios)

    def get_portfolios(self, num: int) -> list[Portfolio]:
        if num == -1 or num == len(self.__Portfolios) + 1:
            return self.__Portfolios
        return [self.__Portfolios[num - 1]]

    def add_portfolio(self, portfolio: Portfolio):
        if portfolio.type == 'portfolio':
            self.__Portfolios.append(portfolio)
        else:
            raise Exception(f'{portfolio} is not an Portfolio')

    def truth_id(self, portfolio: Portfolio, num: int) -> bool:
        index = 0
        for item in self.__Portfolios:
            if (index == num - 1 or num == -1 or num == len(self.__Portfolios) + 1) and portfolio == item:
                return True
            index += 1

    def get_by_num(self, num: int = -1) -> list[Portfolio]:
        if num == -1 or num == len(self.__Portfolios) + 1:
            return self.__Portfolios
        index = 0
        for portfolio in self.__Portfolios:
            if index == num - 1:
                return [portfolio]
            index += 1

    def get_byId(self, find_id: int):
        for portfolio in self.__Portfolios:
            if portfolio.portfolio_id == str(find_id):
                return portfolio
        return "Can't find, incorrect id ("

    def sum_money(self):
        summ = None
        for portfolio in self.__Portfolios:
            if summ is None:
                summ = portfolio.total_amount()
            else:
                summ += portfolio.total_amount()
        if summ is None:
            return "You haven't portfolios"
        return summ
