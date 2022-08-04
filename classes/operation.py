from menu_methods.operation_type import Operation_Type
from tink_data_to_my.operation_state import Operation_State
from tink_data_to_my.tink_data_to_money import money_value_to_float


class Operation:

    def __init__(self, operation_id, parent_operation_id, currency, payment, price, state, quantity, quantity_rest,
                 figi, instrument_type, date, str_type, operation_type, trades):
        self.type = 'operation'
        self.operation_id = operation_id
        self.parent_operation_id = parent_operation_id
        self.currency = currency
        self.payment = money_value_to_float(payment)
        self.price = money_value_to_float(price)
        self.state = Operation_State[state.value]
        self.quantity = quantity
        self.quantity_rest = quantity_rest
        self.figi = figi
        self.instrument_type = instrument_type
        self.date = date.strftime("%d.%m.%Y %H:%M:%S")
        self.str_type = str_type
        self.operation_type = Operation_Type[operation_type.value]

    def __str__(self):
        return f"{self.type}: id операции - '{self.operation_id}', id родительской операции {self.parent_operation_id}, " \
               f"валюта операции - {self.currency}, сумма операции - {round(self.payment, 3)}, цена за одну штуку - {self.price}, " \
               f"количество штук - {self.quantity}, неисполненный остаток по сделке - {self.quantity_rest}, " \
               f"статус операции - {self.state[1]}, тип бумаги - {self.instrument_type}, дата и время операции - {self.date}, " \
               f"тип операции '{self.operation_type[1]}'."
