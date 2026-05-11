rows = int(input("Enter the no of rows: "))
column = int(input("Enter the no of cloumn: "))
symbol = input("Enter a symbol to use: ")



for x in range(rows):
    for y in range(column):
        print(symbol, end="",flush=True)

    print()