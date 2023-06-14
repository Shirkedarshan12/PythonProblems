# Find max & min element in array

# Find Max element in array
arr=[4,7,8,11,13,12]

max=arr[0]   # It will saved first element

for i in range(len(arr)):
    if arr[i] > max:   # here each element in array compare with max variable if it great then
        max=arr[i]     # we will store that element in max it will be contiuned till we get maximum number

print (max)


# Find Min element in array
min=arr[0]

for i in range(len(arr)):
    if arr[i] < min:
        min=arr[i]

print(min)