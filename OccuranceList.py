# Count occurance of an element in list

mylist=[15,6,7,10,12,20,10,10,18,21]

x=10
count=0

for i in mylist:
    if i==x:
        count=count+1

print(f"{x} occured {count} times in list")


