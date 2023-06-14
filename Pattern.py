# Q) write a program for the below pattern with only one while loop?
#
# *
#
# **
#
# ***
#
# ****
#
# *****
#
# ****
#
# ***
#
# **
#
# *


n=5
i=1
direction=1   # for increment

while i>0:
    print("*" * i)

    i+= direction

    if i > n:
        direction =-1
        i-=2

    elif i < 0:
        break
