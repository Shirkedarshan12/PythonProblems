# Write a program to print fibonacci series upto a given number
# fibonacu series = 0,1,1,2,3,5,8,13,21,34,55


n= int(input("Enter your number"))
x=0
y=1
z=0

while (z<=n):
    print(z)
    x=y
    y=z
    z=x+y
