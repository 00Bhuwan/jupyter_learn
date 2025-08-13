'''If this condition is true, execute the code in the clause.'''

# if, elif, else statement are baisc flow control statements in Python.
x = 'ram'


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

a = 'lion bloom family '
print(a.strip())
print(a.strip('lion'))

fruits = ['apple', 'banana', 'cherry']
fruits[0] = 'kiwi'
print(fruits)

mylist = ['apple', 'banana', 'cherry']
mylist1 = mylist.copy()
mylist1.append(['kiwi', 'mango', 'ram', 'shtam'])
print(mylist1, 'using append')
mylist.extend(['kiwi', 'mango', 'ram', 'shtam'])
print(mylist, 'using extend')
print(mylist[2])
mylist.insert(4, 'orange')
print(mylist, '\nadded orange at index 4')

# concat and join are not method of list

mylist.remove('ram')
mylist.pop(-1)
print(mylist, 'after removing ram and last element')  

mylist1.clear()
print(mylist1, 'after clearing mylist1')