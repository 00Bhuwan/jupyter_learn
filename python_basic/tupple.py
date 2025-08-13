''' Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.'''

tup = (1,23,4,5,6,7,8,94)

# TO print each element in the tuple
# i = 0
# while i < len(tup): 
#   print(tup[i])
#   i += 1

tup_list = list(tup)  # convert tuple to list
tup_list.append(100)  # append to the list
print(tup_list)

# convert back to tuple
tup = tuple(tup_list)
print(tup)

fruits = ('apple', 'banana', 'cherry', 'kiwi')
(x, *y) = fruits
(a, *b, c) = fruits
print(y) # Output: ['banana', 'cherry', 'kiwi']
print(b) # Output: ['banana', 'cherry']

# to join
tup2 = tup + fruits
print(tup2)

# to delete tuple
del tup