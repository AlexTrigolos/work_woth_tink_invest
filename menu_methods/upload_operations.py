import datetime

from tinkoff.invest import Client, InstrumentIdType

from classes.all_portfolios import All_Portfolios
from classes.operation import Operation


def upload_operations(client, all_portfolios: All_Portfolios, number: int = -1):
    accounts = client.users.get_accounts().accounts
    account_num = 1
    for account in accounts:
        if number == -1 or number == len(accounts) + 1 or account_num == number:
            for portfolio in all_portfolios.get_by_num(account_num):
                now_date_time = datetime.datetime.now()
                operations = client.operations.get_operations(account_id=account.id, from_=portfolio.get_opened_date(),
                                                              to=now_date_time).operations
                for operation in operations:
                    portfolio.add_operation(Operation(operation.id, operation.parent_operation_id, operation.currency,
                                                      operation.payment, operation.price, operation.state,
                                                      operation.quantity, operation.quantity_rest, operation.figi,
                                                      operation.instrument_type, operation.date, operation.type,
                                                      operation.operation_type, operation.trades))
        account_num += 1
