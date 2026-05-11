#2D lists

fruits = ["apple", "banana", "coconut","pineapple"]
vegetables =["celery", "carrots", "potatoes","cabbage"]
meats = ["chicken", "fish","turkey","beef"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food, end =" ")
    print()
