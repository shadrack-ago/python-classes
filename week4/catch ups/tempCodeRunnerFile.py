def task1():
    user_input=input("Enter a list of integers separated by spaces: ").split()
    integers = [int(i) for i in user_input]
    total = sum(integers)
    print(f"The sum of the integers is: {total}")
task1()