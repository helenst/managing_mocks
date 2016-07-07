from datetime import date


def its_my_birthday():
    today = date.today()
    return today.month == 3 and today.day == 19
