# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
def task1():
    user_input=input("Enter a list of integers separated by spaces: ").split()
    integers = [int(i) for i in user_input]
    total = sum(integers)
    print(f"The sum of the integers is: {total}")
task1()

# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

favorite_books=("Book1", "Book2", "Book3", "Book4", "Book5")
for book in favorite_books:
    print(book)

# Write a program that uses a dictionary to store information about a person,
# such as their name, age, and favorite color.
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.    
def task3():
    person_info = {}
    person_info['name'] = input("Enter your name: ")
    person_info['age'] = int(input("Enter your age: "))
    person_info['favorite_color'] = input("Enter your favorite color: ")
    
    print("Person Information:")
    for key, value in person_info.items():
        print(f"{key}: {value}")

# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.set1 = set(input("Enter integers for first set separated by spaces: ").split())
set2 = set(input("Enter integers for second set separated by spaces: ").split())
common_elements = set.intersection(set2)
print("Common elements:", common_elements)    

# Words with Odd Number of Characters
words = ["apple", "banana", "cat", "dog", "elephant", "fox"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Original words:", words)
print("Words with odd number of characters:", odd_length_words)
