#Execrise 3.12

number = int(input("Enter any five digits number"))
palindrome_number = number
reverse = 0
bool = true

while palindrome_number > 0:
	div = palindrome_number // 10
	reminder = palindrome_number % 10

	palindrome_number = div
	reverse = reverse * 10 + reminder

if reverse == number:
	print (bool)
else:
	bool = fasle
	print (bool)
