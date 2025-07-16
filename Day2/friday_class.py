
print("Enter your dirth of birth")
age = int(input(""))
year = (2000 - age)
print(f"You are: {year} years old")


account_balance = 10000
print("Enter the amount you want to spend")
balance = int(input(""))
remain = account_balance - balance 
print(f"Your balance is remaining: {remain:,.2f}")

about_me = "LovIPyethon"
print(about_me[3:4] + about_me[0:3] + about_me[6:7] + about_me[4:6] + about_me[7:11])
