staff = [("Amit", 20), ("Zara", 20) ,("Raj",25)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible for manage the staff.")
        break
else: # call back logic
    print(f"No one is eligible to mange to staff")