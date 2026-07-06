# inputs:
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the electricity spend = "))
charge_per_unit = int(input("Enter the charges per unit = "))
persons = int(input("Enter the number of person living in a room = "))

# calculations:
total_electricity = electricity_spend * charge_per_unit
total_expense = (rent + food + total_electricity) // persons
electric_bill = electricity_spend*charge_per_unit
monthly_rent = (rent + food + electric_bill)
print(f"totla monthly expences is {monthly_rent}")
print("Total expense per person = ", total_expense)