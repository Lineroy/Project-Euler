# First variant

import math

factorial = 0

for i in str(math.factorial(100)):
    factorial += int(i)

print("First:", factorial)

# Second variant

factorial_main = 1
factorial_result = 0

for fact_num in list(sorted(list(range(1, 101)), reverse=True)):
    factorial_main *= fact_num

for multiplication in str(factorial_main):
    factorial_result += int(multiplication)

print("Second:", factorial_result)