# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list
intergers = list(map(int, input("Enter a list of integers: ").split()))
print("The sum of the integers is: ", sum(intergers))