operator = input("Enter an operator (+ - * /): ")
number1 = float(input("First number: "))
number2 = float(input("Second number: "))

if operator == "+":
    result = number1 + number2
    print(round(result,3))
elif operator == "-":
    result = number1 - number2
    print(round(result,3))
elif operator == "*":
    result = number1 * number2
    print(round(result,3))
elif operator == "/":
    result = number1 / number2
    print(round(result,3))
else:
    print("Error, Invalid Input")
