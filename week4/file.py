# Step 1: Read the contents of input.txt
with open('week4/input.txt', 'r') as input_file:
    content = input_file.read()

# Step 2: Count the number of words in the file
word_count = len(content.split())

# Step 3: Convert all text to uppercase
processed_content = content.upper()

# Step 4: Write the processed text and word count to output.txt
with open('week4/output.txt', 'w') as output_file:
    output_file.write(processed_content)
    output_file.write(f"\n\nWord Count: {word_count}")


# Step 5: Print a success message
print("The file 'output.txt' has been created successfully.")

