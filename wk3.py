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


# Write an if/elif/else statement for a college with a grading system as shown below
# If grade is 90 or higher, print "A"
# Else if grade is 80 or higher, print "B"
# Else if grade is 70 or higher, print "C"
# Else if grade is 60 or higher, print "D"
# Else, print "F"
grade=input("Enter the marks")
grade=int(grade)

if grade>=90&grade<=100:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D") 
elif grade>=1:
     print("F")
else :
        print("Invalid marks")       


# loops
fruits=["apple","banana","cherry"]
for fruit in fruits:
     print(f"fruit is {fruit}")

    #  use range
for i in range(2,8):
    print(i)


# for loop
cars=3
for i in range(cars):
    print(f"car {i}")


# while loop
count=1
while count<=8:
    print(count)
    count+=1
    if count==5:
        break
    else:
        continue

# Example of loop controls: break and continue
for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")    


#print prime numbers between 1 and 20
for num in range(2, 21):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

my_tuple=("a","b","c","d","e","f")
print(my_tuple[-1])
print(my_tuple.index("b"))


# python method that calculate base and expotentiol value and if it is greator than 5000 it return true, else false

def power(base,expotentiol):
  results=base**expotentiol
  if results>5000:
    return True
  else:
    return False

print(power(8,3))    
