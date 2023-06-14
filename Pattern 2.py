n=int(input("enter the number of row: "))

for i in range(1, n+1):  # this for loop we used for rows
    for j in range(1, i+1):
        print(j, end=" ")
    print()