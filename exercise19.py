#collection = single"variable" used to store multiple variable

#List = [] ordered and changable. Duplicates OK
#Set = {} unordered and immutable, but Add/ Remove Ok. No duplicates
#Tuple = () ordered and unchangable. Duplicates OK. FASTER

fruits = ["apple","orange","banana","coconut"]
fruits.append("watermelon")
fruits.insert(4,"pineapple")

fruits.sort()
fruits.reverse()

print(fruits)

for fruit in fruits:
    
    print(fruit)