choice = input("Choose [*,-,+,/]: ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '*':
    total = num1 * num2

elif choice == '-':
    total = num1 - num2

elif choice == '+':
    total = num1 + num2

elif choice == '/':
    total = num1 / num2

else:
    print("You have chosen something I don't know")
    total = None

if total is not None:
    print(f"{num1} {choice} {num2} = {total}")



    