from .masks import get_masked_number


def hide_card_details(bank_card: str) -> str:
    """Функция, которая возвращает исходную строку с замаскированным номером карты/счета"""
    operation_name = []
    nums = []
    replacing_spaces = bank_card.replace(" ", "")
    for card in replacing_spaces:
        if card.isalpha():
            operation_name.append(card)
            connect_name = "".join(operation_name)
        else:
            nums.append(card)
            connect_nums = "".join(nums)
    return f"{connect_name} {get_masked_number(connect_nums)}"


def get_date(date: str) -> str:
    """Функция, которая принимает на вход дату и выводит в необходимом формате"""
    desired_date = date[:10]
    format_the_date = desired_date.split("-")
    year, month, day = format_the_date
    return f"{day}.{month}.{year}"
