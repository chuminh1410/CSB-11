deposit = float(input("Deposit: "))
interest_rate = 0.05

account_1_year = deposit * (1 + interest_rate)
account_2_year = deposit * (1 + interest_rate) ** 2
account_10_year = deposit * (1 + interest_rate) ** 10

print("Account after 1 year:", account_1_year)
print("Account after 2 years:", account_2_year)
print("Account after 10 years:", account_10_year)