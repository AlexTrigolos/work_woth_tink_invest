def menu(client):
    variants = ["Обновить свои портфели.", "Узнайть текущую стоимость всех ценных бумаг.", "Посмотреть 20 последних транзакций.",
                "Операции по каждой из бумаг.", "Посчитать доходность."]
    print("Что хотите?")
    variant = ""
    while variant != "EXIT" and variant != 'УЧШЕ' and (not variant.isdigit() or int(variant) < 1 or int(variant) > len(variants)):
        index = 1
        for vrnt in variants:
            print(f"{index}. {vrnt}")
            index += 1
        print(f"{index}. EXIT.")
        variant = input(f"Введите число 1..{len(variants)} или EXIT: ")
    if variant == "EXIT" or variant == 'УЧШЕ':
        return variant, None
    accounts = client.users.get_accounts().accounts
    if len(accounts) == 0:
        return "У вас нет аккаунтов.", None
    account = ""
    while not account.isdigit() or int(account) < 1 or int(account) > len(accounts) + 1:  # +1 тк есть ариант все
        print("Выберите аккаунт.")
        index = 1
        for item in accounts:
            print(str(index) + ". " + item.name + ".")
            index += 1
        print(str(index) + ". Все аккаунты.")
        account = input(f"Введите число 1..{len(accounts) + 1}: ")
    return int(variant), int(account)
