# How to swap any 2 elements of a list

l=[3,4,7,8,9,11]

# Approach 1
# temp=l[0]
# l[0]=11
# l[5]=temp
# print(l)

# Approach 2
l[0],l[5]=l[5],l[0]
print(l)