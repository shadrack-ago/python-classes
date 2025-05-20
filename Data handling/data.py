

# with open("Data handling/example.txt", "r") as file:
#       data = file.read()
#       print("File content:")
#       print(data)


with open("Data handling/example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1, end='')
    print(line2, end='')  
    
    with open("Data handling/example.txt", "r") as infile:
        content = infile.read()
        word_count = len(content.split())
        upper_content = content.upper()
        print(upper_content, end='')
        print(f"\n\nWord count: {word_count}")

    with open("Data handling/example.txt", "w") as outfile:
        outfile.write(upper_content)
        outfile.write(f"\n\nWord count: {word_count}\n")
