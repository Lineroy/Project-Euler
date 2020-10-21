everything = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

list_with_exceptions_one = list(range(11, 20))
list_with_exceptions_two = list(range(2, 10))

dozens_of_exceptions = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    8: "eighty"
}

units_in_the_period = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    18: "eighteen"
}

quantity_of_letters = 0

for i in range(1, 1000):
    check = str(i).rjust(3, "0")
    if int(check[0]) >= 1:
        if int(check[1:3]) == 0:
            quantity_of_letters += len(everything[int(check[0])] + "hundred")
        else:
            quantity_of_letters += len(everything[int(check[0])] + "hundred and".replace(" ", ""))

    if int(check[1:3]) in list_with_exceptions_one:

        if int(check[1:3]) in units_in_the_period:
            quantity_of_letters += len(units_in_the_period[int(check[1:3])])

        else:
            quantity_of_letters += len(everything[int(check[-1])] + "teen")

    else:
        counter = 1
        for o in check[1:3]:
            if int(check[1]) in list_with_exceptions_two and counter == 1:
                if int(check[1]) in dozens_of_exceptions:
                    quantity_of_letters += len(dozens_of_exceptions[int(check[1])])
                else:
                    quantity_of_letters += len(everything[int(check[1])] + "ty")

                counter += 1

            else:
                quantity_of_letters += len(everything[int(o)])

print(quantity_of_letters + len("one thousand".replace(" ", "")))
