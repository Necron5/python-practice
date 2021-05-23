print("Welcome to my unit converter!")
# Get inches from user
# Convert inches to integer
# Convert inches to centimeter 1 inch = 2.54 cm
# Print cm

input_inch = input("Please input a number of inch: ")
integer_inch = int(input_inch)
number_cm = 2.54 * integer_inch
print(f"{integer_inch} inches are equivalent to {number_cm:.5f} cm.")


# Get pounds from user
# Convert pounds to integer
# Convert pounds to kilogram: 1 kg = 2.2 lb
# Print kg
input_lb = input("Please type a number of lbs: ")
integer_lb = int(input_lb)
number_kg = integer_lb / 2.2
print(f"{integer_lb} lbs are equivalent to {number_kg:.5f} kg.")


# Get fahrenheits from user
# Convert fahrenheits to integer
# Convert fahrenheits celsius: c = (f - 32) * 5/9
# Print celsius

input_f = input("Please type a number of fahrenheit: ")
integer_f = int(input_f)
number_c = (integer_f - 32) * 5 / 9
print(f"{integer_f} fahrenheit degrees are equivalent to {number_c:.5f} celsius degrees.")

# Area
# square feet -> square meters

# Get square feet from user
# Convert square feet to integer
# Convert square feet to square metres: 1 sqft = 0.093 sqmr
# Print square meter

input_sqft = input("Please type a number of square feet: ")
integer_sqft = int(input_sqft)
number_sqmr = integer_sqft * 0.093
print(f"{integer_sqft} square feet are equivalent to {number_sqmr:.5f} square metres")