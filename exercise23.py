#phone keypad generator
num_first = (1, 2 ,3)
num_second = (4, 5, 6)
num_third = (7, 8, 9)
special_char = ("*" ,0, "#")
num_pad = (num_first, num_second, num_third, special_char)

for numbers in num_pad:
    for digit in numbers:
        print(digit, end = "  ")
    print()
