# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
print("Choose hot dog type:")
print("1. Hot dog ($3.50)")
print("2. Chili Dog $4.50)")
choice = int(input("Enter 1 or 2: "))

if choice == 1:
    base_price = 3.50
elif choice == 2:
    base_price = 4.50
else:
    print("Invalid choice.")
    exit()

cheese = input("Add cheese? (yes/no): ").lower() == "yes"
peppers = input("Add peppers? (yes/no): ").lower() == "yes"
onions = input("Add grilled onions? (yes/no): ").lower() == "yes"

toppings_cost = 0
if cheese:
    toppings_cost += 0.50
if peppers:
    toppings_cost += 0.75
if onions:
    toppings_cost += 1.00

subtotal = base_price + toppings_cost 
tax = subtotal * 0.07
total = subtotal + tax

print(f"Hot dog cost: ${subtotal: .2f}")
print(f"Tax: ${tax: .2f}")
print(f"Total cost: ${total: .2f}")
