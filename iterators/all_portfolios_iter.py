class All_Portfolios_Iterator:

    def __init__(self, all_portfolios):
        self._all_portfolios = all_portfolios
        self._index = 0

    def __next__(self):
        if self._index < len(self._all_portfolios):
            result = self._all_portfolios[self._index]
            self._index += 1
            return result
        raise StopIteration
