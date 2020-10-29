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
