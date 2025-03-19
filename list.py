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

prime_numbers=[2,3,5,7]
even_numbers=[4,6,8]
prime_numbers.extend(even_numbers)
print("after extending",prime_numbers)

numbers=even_numbers+prime_numbers
print("after adding",numbers)

del prime_numbers[2]
print("after deleting",numbers)

prime_numbers.remove(3);

even_numbers.pop(1)
print("after popping",even_numbers)

even_numbers.insert(2,10)
print("after pushing",even_numbers)

# Python Tuple
letters=('a','b','c','d', 'a','e')
print(letters)

print(letters.count('a'))
print(letters.index('d'))

# Python dictionary
province={"kisumu":"Nyanza","Nairobi":"Nairobi","Mombasa":"Coast"}
print(province)
province["Nakuru"]="Rift Valley"
print(province)
province["Garissa"]="North Eastern"

# python sets
A={1,2,3,4,5,9}
B={4,5,2,6,7,8}
print(A.union(B))
# or
print(A|B)
print(A.intersection(B))
# or
print(A&B)
print(A.difference(B))
# or
print(A-B)
print(A.symmetric_difference(B))
# or
print(A^B)

if 1 in A:
    print("1 is in A");

C={1,2,3}
D={3,2,1}
# perform difference operation
if C==D:
    print("set C is equal to set D")
else:
    print("set C is not equal to set D")
