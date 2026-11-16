#Exercise 2.10

num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))
num_3 = int(input("Enter second number"))

sum = num_1 + num_2 + num_3

average = num_1 + num_2 + num_3 // 3

product = num_1 *  num_2 * num_3

 min_num = num_2
 max_num = num_1

#smallest number
if (num_1 < min_num):
     min_num = num_1
If (num_3 < min_num):
      min_num = num_3

#largest number
if (num_3 > max_num):
     max_num = num_3
if (num_2 > max_num):
     max_num = num_2

print(f"Sum: {sum}\n Average: {average}\n Product: (product}\n Smallest Number: {min_num}\n Largest Number: {max_num}")
