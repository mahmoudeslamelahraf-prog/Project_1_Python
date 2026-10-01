choice = input("choose [*,-,+,/]")


if choice == '*':
    print("MULTIPLYING")
elif choice == '-':
    print("MINUS")
elif choice == '+':
    print("PLUS")
elif choice == '/':
    print("divide")
else:
    print("you have choosed something i don't know ")

num1 = int(input("Enter the frist number: "))
num2 = int(input("Enter the sec number: "))
total = num1 + num2
print(f"{num1} + {num2} = {total}")

