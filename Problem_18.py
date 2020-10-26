import random
import math

triangle = """
                                        75
                                      95 64
                                    17 47 82
                                  18 35 87 10
                                20 04 82 47 65
                              19 01 23 75 03 34
                            88 02 77 73 07 63 67
                          99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                    53 71 44 65 25 43 91 52 97 51 14
                  70 11 33 28 77 73 17 78 39 68 17 57
                91 71 52 38 17 14 91 43 58 50 27 29 48
              63 66 04 68 89 53 67 30 73 16 69 87 40 31
            04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".replace(" ", "").replace("\n", " ").split()

step_one, step_two, step_three = [], [], []

counter = 1

for i in triangle:
    slice_from, slice_to = 0, 2
    tuple_to = []
    for o in range(1, math.ceil(len(i) / 2) + 1):
        tuple_to.append(i[slice_from:slice_to])
        slice_from += 2
        slice_to += 2

    step_one.append(tuple([int(i) for i in tuple_to]))

for i in step_one:
    result = []
    slice_from, slice_to = 0, 2
    for o in i:
        try:
            result.append((o, (step_one[counter][slice_from:slice_to])))
            slice_from += 1
            slice_to += 1
        except IndexError:
            break

    step_two.append(result)
    counter += 1

del step_two[-1]

for i in step_two:
    to_append = []
    for o in i:
        for u in o:
            to_append.append(u)

    step_three.append(to_append)

main_result = []
adding_to_the_main = [75]

while len(main_result) != 16384:
    for i in step_three:
        rand_number = random.randint(0, 1)
        adding_to_the_main.append(int(i[i.index(adding_to_the_main[-1]) + 1][rand_number]))

    main_result.append(sum(adding_to_the_main))
    to_main = 0
    adding_to_the_main = [75]

print(max(main_result))
