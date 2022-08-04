class PricePaper:

    def __init__(self, currency, price):
        self.currency = currency
        self.price = price

    def __str__(self):
        if self.currency == 'rub':
            return str(self.price) + u" \N{ruble sign}"
        elif self.currency == 'usd':
            return str(self.price) + u" \N{dollar sign}"
        elif self.currency == 'eur':
            return str(self.price) + u" \N{euro sign}"
        return self.currency + " " + str(self.price)

    def __mul__(self, other):
        return PricePaper(self.currency, self.price * other)

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception(f"PricePaper add currency not the same {self.currency} and {other.currency}")
        return PricePaper(self.currency, self.price + other.price)

    def __round__(self, n=None):
        return PricePaper(self.currency, round(self.price, n))
