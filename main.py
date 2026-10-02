import random

WIDTH = 680
HEIGHT = 400

numbers = "number.txt"
open_numbers= open(numbers, "r")
read_numbers= open_numbers.readlines()
sum = 0
for i in read_numbers:
    sum += int(i)

open_numbers.close()

print(sum)