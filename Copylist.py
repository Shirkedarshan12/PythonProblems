# How to copy a list

#Approach1  Using Slicing Technique

# mylist=[4,7,11,13,56,16]
# mylist_copy= mylist[:]
# print(mylist_copy)

#Approach 2 Using Extend Method

mylist=[9,3,5,8,11,13]
mylist_copy=[]
mylist_copy.extend(mylist)
print(mylist_copy)