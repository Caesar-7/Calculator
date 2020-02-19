# Created by Caesar-7 19/02/2020 dd/mm/yy

from math import sin,cos,tan,sqrt,radians

op1 = ("sin","cos","tan","sqrt")
op2 = ("+","-","*","/","**","^")

rtype = input("Type of result: ")
n1 = float(input("First number: "))
op = input("Operator: ")

if op in op1:
	if op == "sin":
		n1 = radians(n1)
		r = sin(n1)
	elif op == "cos":
		n1 = radians(n1)
		r = cos(n1)
	elif op == "tan":
		n1 = radians(n1)
		r = tan(n1)
	elif op == "sqrt":
		r = sqrt(n1)
elif op in op2:
	n2 = float(input("Second number: "))
	if op == "+":
		r = n1 + n2
	elif op == "-":
		r = n1 - n2
	elif op == "*":
		r = n1 * n2
	elif op == "/":
		r = n1 / n2
	elif op == "**" or op == "^":
		r = n1 ** n2
else:
	raise ValueError("Operator not supported")

if rtype == "int":
	print(int(r))
elif rtype == "float":
	print(r)
elif rtype == "round":
	nround = input("Round: ")
	print(round(r, int(nround)))
else:
	raise ValueError("Type not supported")
