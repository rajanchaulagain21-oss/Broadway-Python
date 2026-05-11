#compound interest calculator 
principal = 0
rate = 0
time = 0
while True:
    principal = int(input("Enter Principal Amount: "))
    if principal < 0:
        print("Principal cannot be less than zero")

    else:
        break
    

while True:
    rate = int(input("Enter rate in %: "))
    if rate < 0 :
        print("Rate cannot be less than zero")
    else:
        break

while True:
    time = int(input("Enter time in years: "))
    if time < 0:
        print("time cannot be less than to zero")

    else:
        break

compound_amount = principal*(1 + rate/100)**time
compound_interest = compound_amount - principal
print(f"The compound amount is ${compound_amount:.2f}")
print(f"The compound interest is ${compound_interest:.2f}")