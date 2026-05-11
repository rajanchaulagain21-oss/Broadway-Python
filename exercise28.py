#food truck program

menu = {"small-pizza": 480,
        "burger": 180,
        "chicken momo": 120,
        "veg momo": 100,
        "chowmein": 80,
        "chicken wings": 70}

list = []
total = 0

for key, value in menu.items():
    print(f"{key:20}: {value:.2f}")
while True:
    food = input("Enter food you like to buy (q to quit): ") 
    if food.lower() == "q":
        break
    elif menu.get(food) != None:
        list.append(food)
        
for food in list:
    total = total + menu.get(food)
    print(food,end =" ")
print()
print("-------------------------")
print(f"Total = Rs{total}")
