#Calculator Program


print("""What would you like to do ?
      Type:
      + for addition
      - for substraction
      * for multiplication
      / for division""")
operation = input(">>>>>>>: ")
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
if operation == "+":
    result= num1 + num2
    print(f"Output = {result:.2f}")


elif operation=="-":
    result= num1 - num2
    print(f"Output = {result:.2f}")

elif operation=="*":
    result= num1 * num2
    print(f"Output = {result:.2f}")

elif operation=="/":
    result= num1 / num2
    print(f"Output = {result:.2f}")
else:
    print("please type in correct operator!!")
