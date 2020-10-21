list_of_numbers = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48""".split()

for i in list_of_numbers:
    a = list_of_numbers.index(i)
    if i[0] == "0":
        list_of_numbers.remove(i)
        list_of_numbers.insert(a, i[1])

list_of_numbers = [int(i) for i in list_of_numbers]

own_list_of_ALL_numbers = []

list_for_everything = []
not_good = sorted(list(range(17, 399, 20)) + list(range(18, 399, 20)) + list(range(19, 399, 20)))

dig_st, dig_nd, dig_rd = 20, 40, 60
slicing_from, slicing_to = 0, 4

counter_index = 0

diagonal_back = [8, 91, 77, 50, 12, 52, 78, 7, 5, 4, 75, 0, 40, 0, 15, 38, 97, 22, 2, 8, 0, 62, 56, 4, 48, 69, 43, 98,
                 40, 17, 87, 60, 57, 18, 81, 17, 40, 99, 49, 49, 65, 36, 13, 49, 3, 30, 88, 53, 67, 40, 71, 93, 29, 14,
                 79, 55, 73, 31, 49, 81, 91, 36, 2, 37, 71, 56, 32, 1, 56, 68, 24, 69, 42, 11, 60, 4, 23, 95, 70, 52,
                 80, 13, 33, 66, 28, 40, 40, 22, 54, 36, 92, 41, 89, 63, 67, 51, 71, 16, 31, 22, 50, 12, 17, 35, 20, 84,
                 36, 78, 53, 33, 75, 44, 2, 45, 3, 99, 60, 32, 47, 24, 70, 64, 38, 18, 66, 70, 54, 59, 67, 40, 38, 26,
                 10, 67, 23, 64, 28, 81, 98, 32, 21, 94, 49, 66, 91, 40, 8, 63, 39, 94, 63, 95, 20, 12, 62, 2, 68, 20,
                 26, 67, 72, 63, 89, 34, 88, 14, 83, 96, 78, 78, 17, 97, 26, 99, 73, 66, 5, 58, 55, 24, 95, 33, 31, 34,
                 97, 33, 61, 0, 14, 35, 45, 20, 44, 76, 0, 75, 9, 23, 36, 21, 92, 56, 53, 9, 14, 16, 62, 4, 80, 3, 94,
                 15, 67, 31, 75, 22, 28, 53, 17, 78, 57, 85, 29, 36, 24, 54, 17, 0, 24, 88, 58, 55, 47, 31, 35, 96, 42,
                 5, 39, 16, 58, 17, 54, 51, 58, 21, 60, 44, 37, 44, 44, 5, 7, 89, 71, 35, 48, 0, 56, 86, 40, 55, 89, 4,
                 77, 17, 52, 86, 13, 92, 73, 28, 69, 47, 94, 5, 68, 81, 80, 19, 66, 98, 27, 33, 79, 26, 26, 16, 32, 57,
                 97, 7, 16, 99, 35, 97, 83, 8, 52, 4, 69, 53, 93, 63, 32, 12, 55, 46, 67, 33, 46, 3, 72, 20, 62, 57, 87,
                 68, 36, 88, 36, 76, 62, 40, 32, 29, 46, 8, 18, 72, 94, 24, 11, 39, 25, 38, 73, 16, 42, 4, 16, 36, 4,
                 74, 85, 59, 67, 82, 69, 99, 62, 34, 88, 23, 30, 72, 41, 36, 69, 20, 54, 5, 57, 23, 16, 81, 86, 48, 71,
                 49, 31, 74, 1, 90, 31, 78, 29, 35, 73, 20, 48, 67, 19, 89, 1, 52, 43, 61, 48, 33, 92, 16, 69, 54, 51,
                 83, 71, 54, 70, 1]

while True:
    b = 1
    # Slice right.
    for i in [int(i) for i in list_of_numbers[slicing_from:slicing_to]]:
        b *= i
    list_for_everything.append(b)
    slicing_to += 1
    slicing_from += 1
    if slicing_to >= len(list_of_numbers):
        own_list_of_ALL_numbers.append(max(list_for_everything))
        list_for_everything.clear()
        slicing_from, slicing_to = 0, 4

    # Slice left.
    list_of_numbers.reverse()
    b = 1
    for i in [int(i) for i in list_of_numbers[slicing_from:slicing_to]]:
        b *= i
    list_for_everything.append(b)
    slicing_to += 1
    slicing_from += 1
    if slicing_to >= len(list_of_numbers):
        own_list_of_ALL_numbers.append(max(list_for_everything))
        list_for_everything.clear()
        slicing_from, slicing_to = 0, 4

    # Slice down.
    try:
        for slice_down in list_of_numbers:
            list_for_everything.append(slice_down * list_of_numbers[dig_st] * list_of_numbers[dig_nd] *
                                       list_of_numbers[dig_rd])

            dig_st += 1
            dig_nd += 1
            dig_rd += 1
    except IndexError:
        own_list_of_ALL_numbers.append(max(list_for_everything))
        list_for_everything.clear()
        dir_st, dig_nd, dig_rd = 20, 40, 60
        pass

    # Slice up.
    try:
        for slice_up in list_of_numbers[::-1]:
            list_for_everything.append(slice_up * list_of_numbers[dig_st] * list_of_numbers[dig_nd] *
                                       list_of_numbers[dig_rd])
            dig_st += 1
            dig_nd += 1
            dig_rd += 1
    except IndexError:
        own_list_of_ALL_numbers.append(max(list_for_everything))
        dig_st, dig_nd, dig_rd = 20, 41, 62
        pass

    # Slice diagonally to the right.
    try:
        for slice_dig_right in list_of_numbers:
            counter_index += 1
            dig_st += 1
            dig_nd += 1
            dig_rd += 1
            if counter_index - 1 in not_good:
                pass
            else:
                list_for_everything.append(slice_dig_right * list_of_numbers[dig_st] * list_of_numbers[dig_nd] *
                                           list_of_numbers[dig_rd])

    except IndexError:
        own_list_of_ALL_numbers.append(max(list_for_everything))
        list_for_everything.clear()
        dig_st, dig_nd, dig_rd = 20, 41, 62
        counter_index = 0
        pass

    # Diagonal cut to the left.
    try:
        for dig_left in diagonal_back:
            counter_index += 1
            dig_st += 1
            dig_nd += 1
            dig_rd += 1
            if counter_index - 1 in not_good:
                pass
            else:
                list_for_everything.append(dig_left * diagonal_back[dig_st] * diagonal_back[dig_nd] *
                                           diagonal_back[dig_rd])

    except IndexError:
        own_list_of_ALL_numbers.append(max(list_for_everything))
        print(max(own_list_of_ALL_numbers))
        break

