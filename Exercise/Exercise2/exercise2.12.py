#Exercise

rate = 0.07
year_1 = 10
year_2 = 20
year_3 = 30
principal = 1000

amount_1 = principal * (1 + rate) ** 10
amount_2 = principal * (1 + rate) ** 20
amount_3 = principal * (1 + rate) ** 30

print(f"First amount: {amount_1:.2f} \n Second amount: {amount_2:.2f} \n Third amount: {amount_3:.2f}")
