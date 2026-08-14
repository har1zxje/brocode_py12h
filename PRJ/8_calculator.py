operator = input("enter a operator (+ - * /): ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operator == "+":
    print(f"tong 2 so la {round((num1 + num2),2)}")
elif operator == "-":
    print(f"hieu 2 so la {round((num1 - num2),2)}")
elif operator == "*":
    print(f"nhan 2 so la {round((num1 * num2),2)}")
elif operator == "/":
    print(f"chia 2 so la {round((num1 / num2),2)}")
else: 
    print(f"{operator} is not a valid operator!")