#Exercise 3.13

number = int(input("Enter any integer: "))

factorial = 1

for num in range(number, 0, -1):
#	print (num)
	factorial = factorial * num

print (f"Factorial of {number}: {factorial}")
