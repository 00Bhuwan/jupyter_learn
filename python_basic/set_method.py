'''Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unchangeable, but you can remove items and add new items.'''

# set cannot have same value twice
# cannot acces items using index
list1 = [1, 2, 3, 4, 5, 5, 2, 8, 9]
set1 = set(list1)
print(f'{list1} \n{set1}')

set1.add(10)  # add an item
# set1.insert(11)  # insert an item gives error not supported in sets
# set1.append(12)  # append an item gives error not supported in sets
print(set1)