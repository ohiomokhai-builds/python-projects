#Exercise 2.15

num_1 = float(input("Enter any decimal number: ")
num_2 = float(input("Enter any decimal number: ")
num_3 = float(input("Enter any decimal number: ")

if num_1 <= num_2 <= num_3:
    print(num_1, num_2, num_3)
elif num_1 <= num_3 <= num_2:
    print(num_1, num_3, num_2)
elif num_2 <= num_1 <= num_3:
    print(num_2, num_1, num_3)
elif num_2 <= num_3 <= num_1:
    print(num_2, num_3, num_1)
elif num_3 <= num_1 <= num_2:
    print(num_3, num_1, num_2)
else:
    print(num_3, num_2, num_1)
