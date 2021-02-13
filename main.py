print("Welcome to the tip calculator!")

total_bill = input("What is the total bill? ")
people = input("How many people to split the bill? ")
tip = input("What is % tip you want to give? ")

total_tip = int(tip) / 100 * int(total_bill)

bill_with_tip = int(total_bill) + int(total_tip)

individual_total = int(bill_with_tip) / int(people)

print(f"The total tip is ${round(total_tip)}")
print(f"The total bill with tip is ${round(bill_with_tip)}")
print(f"You have to contribute ${round(individual_total)} towards the total bill")