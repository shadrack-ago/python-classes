temperature=20
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")    

# elif statement
temperature = 20
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
elif temperature < 20:
    print("It's a cool day")
else:
    print("It's a warm day")

# loops    
fruits = ["apple", "banana", "cherry"]
print(f"The fruit: {fruits[0:len(fruits)]}")  # Using len to get all fruits
print(f"The reverse fruit: {fruits[len(fruits)-1::-1]}")  # Using len to reverse the list