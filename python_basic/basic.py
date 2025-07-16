''' if you try to use the + operator on a string and an integer value '''
# print('hello' + 12)  # this will raise a Type Error

''' if you try to use the * operator on a string and an integer value '''
print('hello' * 12)  # this will replicate the string the multiplied number of times

''' if you try to use the * operator on two strings '''
# print('hello' * 'world')  # this will raise a Type Error

''' if you try to use the * operator on a string and an float value '''
# print('hello' * 2.5)  # this will raise a Type Error

''' if you try to add a integer value with float it results in a float '''
print(type(12 + 0.5))  # <class 'float'>

print('what is your name?')
my_name = input('> ')
print("It's nice to meet you, " + my_name + "!")

spam = input()
print(type(spam), spam)
spam = int(spam)  # convert the input to an integer
print(type(spam), spam)
''' if input is integer it will show result but if input is string or float it will raise a value error '''
