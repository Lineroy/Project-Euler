"""
Дана следующая информация (однако, вы можете проверить ее самостоятельно):

    1 января 1900 года - понедельник.
    В апреле, июне, сентябре и ноябре 30 дней.
    В феврале 28 дней, в високосный год - 29.
    В остальных месяцах по 31 дню.
    Високосный год - любой год, делящийся нацело на 4,
    однако последний год века (ХХ00) является високосным в том и только том случае, если делится на 400.

Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?
"""

import datetime

year = 1900

sundays = 0

while year != 1999:
    month = 1
    while month != 13:
        if datetime.datetime(year, month, 1).isoweekday() == 7:
            sundays += 1

        month += 1

    year += 1

print(sundays)