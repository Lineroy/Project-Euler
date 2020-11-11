file = open("p022_names.txt", "r")
file = sorted(str(*file).replace(",", " ").replace('"', "").split())

points = 0

letters = "abcdefghijklmnopqrstuvwxyz"

for names in file:
    symbols_sum = 0
    for symbols in names.lower():
        symbols_sum += ord(symbols) - 96

    points += symbols_sum * (file.index(names) + 1)

print(points)