import sys

group_size = 1

try:
    group_size = int(input("How many people are in the group? "))
except:
    print("ERROR: Please enter an integer.")
    sys.exit(1)

guests = []

for i in range(1, group_size + 1):
    guest = input(f"Enter person {i}'s name: ")
    guests.append(guest)

bill_amount = float(input("How much was the bill? "))

split_bill = round(bill_amount / group_size, 2)

print('=' * 50)
print(f'Total Bill: ${bill_amount}')
for g in guests:
    print(f'{g} owes ${split_bill}.')
print("=" * 50)

