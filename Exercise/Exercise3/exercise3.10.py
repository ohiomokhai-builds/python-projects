#Exercise 3.10

#amount = "p(1 + r)"**r

for number in range (1, 31):
    amount = 1000 * (1 + 0.07) ** number
    print (f"For year {number}, the amount is ${amount:.2f}")
