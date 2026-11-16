#Exercise 3.8

count = 0
int_sum = 0
product = 1
num_count = 0

num_one = 1
num_two = 1
num_three = 1
num_four = 1

while count <= 3:

    num = int(input("Enter any integer: "))
    int_sum = int_sum + num
    product = product * num

    if count == 0:
        num_one = num
    elif count == 1:
        num_two = num
    elif count == 2:
        num_three = num
    elif count == 3:
        num_four = num

    count += 1
    num_count += 1

average = int_sum // num_count

print(int_sum)
print(product)
print(average)

smallest_number = min(num_one, num_two, num_three, num_four)
largest_number = max(num_one, num_two, num_three, num_four)

print("Smallest:", smallest_number)
print("Largest:", largest_number)
