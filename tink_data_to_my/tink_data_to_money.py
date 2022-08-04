from classes.price_paper import PricePaper


def quotation_to_float(quantity) -> float:
    return quantity.__dict__['units'] + quantity.__dict__['nano'] / 1_000_000_000


def money_value_to_float(current_price) -> PricePaper:
    return PricePaper(current_price.__dict__['currency'],
                      current_price.__dict__['units'] + current_price.__dict__['nano'] / 1_000_000_000)
