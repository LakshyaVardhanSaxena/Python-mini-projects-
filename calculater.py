def calculator():
	num1 = float(input("Enter first number: "))
	operator = input("Enter operator (+, -, *, /): ")
	num2 = float(input("Enter second number: "))

	if operator == '+':
		result = num1 + num2
	elif operator == '-':
		result = num1 - num2
	elif operator == '*':
		result = num1 * num2
	elif operator == '/':
		if num2 != 0:
			result = num1 / num2
		else:
			print("Error! Division by zero is not allowed.")
			return
	else:
		print("Invalid Operator!")
		return

	print("Result:", result)

calculator()
