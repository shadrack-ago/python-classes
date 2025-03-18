# list declarations
my_list=[1,2,3,4,5]
print(my_list)
print(my_list[0])

my_list[2]=10
print(my_list[2])

languages=['C','C++','Java','Python']
print(languages[-2])
print(languages[1:3])
print(languages[:]) #prints all elements

# my_list[2:5] returns a list with items from index 2 to index 4.
# my_list[5:] returns a list with items from index 1 to the end.
# my_list[:] returns all list items

my_list.append(6)
print("after appending", my_list)

my_list.insert(3,7)
print("after inserting", my_list)
# so insert you can insert at any index but indicate the position