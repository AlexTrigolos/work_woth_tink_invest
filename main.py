from tinkoff.invest import Client

from menu_methods.current_value_all_securities import find_current_value_all_securities
from menu_methods.menu import menu
from menu_methods.upload_operations import upload_operations
from menu_methods.upload_portfolios import upload_portfolios
from read_token import read_token

TOKEN = ""

if __name__ == '__main__':
    TOKEN = read_token()
    with Client(TOKEN) as client:
        all_portfolios = None
        last_account = None
        while True:
            variant, account = menu(client)
            if variant == "EXIT" or variant == 'УЧШЕ':
                break
            elif variant == 1:
                all_portfolios = upload_portfolios(client, account)
                print(all_portfolios)
            elif variant == 2:
                if all_portfolios is None or last_account != account:
                    all_portfolios = upload_portfolios(client, -1)
                    last_account = account
                find_current_value_all_securities(client, all_portfolios, account)
            elif variant == 3:
                if all_portfolios is None or last_account != account:
                    all_portfolios = upload_portfolios(client, -1)
                    last_account = account
                upload_operations(client, all_portfolios, account)
                for portfolio in all_portfolios.get_portfolios(account):
                    portfolio.show_operations(20)
            elif variant == 4:
                if all_portfolios is None or last_account != account:
                    all_portfolios = upload_portfolios(client, -1)
                    last_account = account
                for item in all_portfolios.get_portfolios(account):
                    if item.count_operations() == 0:
                        upload_operations(client, all_portfolios, account)
                        break
                for item in all_portfolios.get_portfolios(account):
                    item.show_time_paper(client)
            elif variant == 5:
                pass
            else:
                print(f"WTF {variant}, {account}")
            last_account = account
            print("Нажмите enter для продолжения.")
            input()
