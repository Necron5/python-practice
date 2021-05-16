print("Welcome to use my bill calculator!")
# Get bill amount from user
# Get tip percentage from user
# Get tax rate from user
# Get number of people in user's group
# Covert all inputs to integer
# Calculate tip: bill_amount * tip_percentage / 100
# Calculate tax: bill_amount * tax_rate / 100
# Calculate total amount
# Calculate how much each person should pay
# Print information

input_bill = input("How much for your meal?: ")
input_tip_rate = input("What percentage you want to pay for tip?: ")
input_tax_rate = input("What is the tax rate in your area?: ")
input_num_people = input("How many persons are in your group?: ")

float_bill = float(input_bill)
int_tip_rate = int(input_tip_rate)
int_tax_rate = int(input_tax_rate)
int_num_people = int(input_num_people)

tip = float_bill * int_tip_rate / 100
tax = float_bill * int_tax_rate / 100
total_amount = float_bill + tip + tax

amount_each_person = total_amount / int_num_people
tip_each_person = tip / int_num_people

print(f"{int_num_people} persons, Total amount: ${total_amount:.2f}, Amount for each person: ${amount_each_person:.2f}, Tip for each person: ${tip_each_person:.2f}")