#List = [] ordered and changable. Duplicates OK
#Set = {} unordered and immutable, but Add/ Remove Ok. No duplicates
#Tuple = () ordered and unchangable. Duplicates OK. FASTER

fruits = {"apple","orange","banana","coconut"}
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()



print(fruits)

for fruit in fruits:
    
    print(fruit)


fruits_tuple = ("apple","orange","banana","coconut","apple")
print(fruits_tuple.count("apple"))
print(fruits_tuple.index("orange"))