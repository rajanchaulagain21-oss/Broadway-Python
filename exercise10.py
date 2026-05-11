#Temperature conversion program

print("                         TEMPERATURE CONVERSION PROGRAM                       ")

print("""Press
1 - To convert Celcius to Farenheit
2 - To convert Celcius to Kelvin
3 - To convert Farenheit to Celcius
4 - To convert Farenheit to Kelvin
5 - To convert Kelvin to Celcius
6 - To convert Kelvin to Farenheit""")

conversion = input(">>>>>>: ")
temp = float(input("Enter temperature: "))

if conversion == "1":
    result = (temp * 9/5) + 32


elif conversion == "2":
    result = temp + 273.15

elif conversion == "3":
    result = (temp - 32) * 5/9

elif conversion == "4":
    result = (temp - 32) * 5/9 + 273.15

elif conversion == "5":
    result = (temp - 273.15)

elif conversion == "6":
    result = (temp - 273.15) * 9/5 + 32

else:
    print("Please type number as per instruction!")

print(f"Your converted temperature is {result:.2f}")

      