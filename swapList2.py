# How to swap any 2 element in list
l=[4,5,8,11,13,17]

# Approach 1
# temp=l[1]
# l[1]=11
# l[3]=temp
# print(l)

# Approach 2
l[1],l[3]=l[3],l[1]
print(l)