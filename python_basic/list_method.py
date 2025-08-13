mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i += 1

print('reversed list')
for i in reversed(mylist):
  print(i)

nums= [5, 2, 9, 1, 5, 6]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True) #OR
# nums.reverse()
print(nums)

# to copy a list
mylist2 = mylist.copy()
mylist3 = list(mylist)
mylist4 = mylist[:]
print(mylist2, mylist3, mylist4) #but give whitespace in each new line output
print(f"{mylist2} \n{mylist3} \n{mylist4}") #doesn't give whitespace in each new line output

new_list = mylist + nums
print(new_list)
mylist.extend(nums) #extend the list
print(mylist)