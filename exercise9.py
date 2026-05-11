#Python weight converter


print("""Press 1 to convert lbs to kg
Press 2 to convert kg to lbs""")
conversion = input(">>>>>: ")

if conversion == "1":
    weight = float(input("Enter your weight in lbs: "))
    output = weight * 0.45
    print(f"Your weight in Kilogram is {output:.2f}kg.")
elif conversion == "2":
    weight = float(input("Enter your weight in kg: "))
    output = weight / 0.45
    print(f"Your weight in Pound is {output:.2f}lbs.")
else:
    print("Please type in either 1 or 2 !!!")
