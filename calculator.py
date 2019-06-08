# Created by Caesar 2/06/2019

# Sintax of the input:
# Type of result (int, float, roundFloat)
# Operator (+, -, *, /, pow, sqrt, sin, cos, tan)
# First number
# Type of input, only if you chose sin, cos or tan (deg, rad)
# Second number, only if you chose an operator that needs two values
# Number of digits of the result, only if you chose roundFloat ("unit" if you want
# to round at the unit, or specify how many digits you want)

import math as mt
numType = input("Type of result: ")
op = input("Operator: ")
num1 = float(input("First number: "))

if op == "+":
    num2 = float(input("Second number: "))
    r = num1 + num2
elif op == "-":
    num2 = float(input("Second number: "))
    r = num1 - num2
elif op == "*":
    num2 = float(input("Second number: "))
    r = num1 * num2
elif op == "/":
    num2 = float(input("Second number: "))
    r = num1 /num2
elif op == "pow":
    num2 = float(input("Second number: "))
    r = mt.pow(num1, num2)
elif op == "sqrt":
    r = mt.sqrt(num1)
elif op == "sin":
    inputType = input("Type of input: ")
    if inputType == "deg":
        num1 = mt.radians(num1)
        r = mt.sin(num1)
    elif inputType == "rad":
        r = mt.sin(num1)
    else:
        print("Not supported")
elif op == "cos":
    inputType = input("Type of input: ")
    if inputType == "deg":
        num1 = mt.radians(num1)
        r = mt.cos(num1)
    elif inputType == "rad":
        r = mt.cos(num1)
    else:
        print("Not supported")
elif op == "tan":
    inputType = input("Type of input: ")
    if inputType == "deg":
        num1 = mt.radians(num1)
        r = mt.tan(num1)
    elif inputType == "rad":
        r = mt.tan(num1)
    else:
        print("Not supported")
else:
    print("Error")

if numType == "int":
    print(int(r))
elif numType == "float":
    print(float(r))
elif numType == "roundFloat":
    numRound = input("Round: ")
    if numRound == "unit":
        print(round(r))
    else:
        print(round(r, int(numRound)))
else:
    print("Not supported")
