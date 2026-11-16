#Exercise 3.9

number = int(input("Enter any five digits integer: "))

divisor = 10000

while 0 < number:

	div = number // divisor
	reminder = number % divisor
	number = reminder

	print(f"{div}")

	divisor = divisor // 10
