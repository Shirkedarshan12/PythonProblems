# Find factorial of number
#
# factorial means 5= 5*4*3*2*1

i= int(input("Enter your number"))
fac=1   # multplication start with 1

while (i>0):
    fac=fac*i
    i-=1

print("Factorial =", fac)

