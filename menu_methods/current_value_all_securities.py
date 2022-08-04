from tinkoff.invest import Client

from classes.all_portfolios import All_Portfolios


def find_current_value_all_securities(client, all_portfolios: All_Portfolios, number: int = -1):
    accounts = client.users.get_accounts().accounts
    account_num = 1
    for account in accounts:
        if number == -1 or number == len(accounts) + 1 or account_num == number:
            for portfolio in all_portfolios.get_by_num(account_num):
                portfolio.show_total_amount_everyone()
        account_num += 1
    print("Хотите узнать о каждой бумаге? (да/нет)")
    inpt = ""
    while inpt != 'да' and inpt != 'нет' and inpt != 'lf' and inpt != 'ytn':
        inpt = input()
    if inpt == 'да' or inpt == 'lf':
        for portfolio in all_portfolios.get_by_num(number):
            print(portfolio)
