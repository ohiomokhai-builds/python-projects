#Exercise 2.11

number = int(input("Enter any five digits: i.e 12345"))

divisor = 10000

while number > 0:

        div = number // divisor

	print (div)

        reminder = number % divisor

	number = reminder

        divisor = divisor // 10
 
