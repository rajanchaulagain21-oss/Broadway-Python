# format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3.1458
price2 = 895.36
price3 = 45.65

print(f"Price 1 is ${price1:<10.2f}")
print(f"Price 2 is ${price2:>10.2f}")
print(f"Price 3 is ${price3:^10.2f}")