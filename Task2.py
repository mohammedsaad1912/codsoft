print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))

if(option in [1,2,3,4]):
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    if(option == 1):
        add = num1 + num2
        print(f"The Addition Of Two Number: {add}")
    elif(option == 2):
        sub = num1 - num2
        print(f"The Subtraction Of Two Number: {sub}")
    elif(option == 3):
        mul = num1 * num2
        print(f"The Multiplication Of Two Number: {mul}")
    elif(option == 4):
        div = num1 / num2
        print(f"The Division Of Two Number: {div}")
else:
    print("Invalid Operation Entered")

