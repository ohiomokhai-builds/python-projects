#Exercise 3.7

print("Number\t", "Square\t", "Cube\t ")

for number in range (6):
	square = number**2
	cube = number**3
	print(f"{number:>6} {square:>8} {cube:>5}")

