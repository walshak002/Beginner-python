#IF AND ELSE STATEMENT

score = int(input("Please enter score: \n"))
credit = int(input("Please enter number of suject pass: \n"))
subject = input("Enter suject pass(Maths, English, Chemistry): \n")

if score >= 70  and credit >= 5 and subject == "Maths":
  print("Admission granted")

else:
  print("Admission denied")

balance = 5000

user = int(input("Please enter your PIN: \n"))
if user == 1234:
  print("PIN is correct")
else:
  print("Invalid PIN, Access denied")

money = int(input("How much do you want to withdraw: \n"))
if money >= balance:
  print("Insuffient funds")

elif money <= balance:
  print("Take your cash")
'''

