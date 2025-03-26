# statement that gives discounts on goods above 2000
bill=input("enter the bill amount:")
bill=int(bill)
# bill=2500
if bill>2000:
    discount=bill*0.1
    print("Discount is ",discount)
    bill=bill-discount
    print("New bill is ",bill)
else:
    print("No discount for;")

print(f"Bill is {bill}")