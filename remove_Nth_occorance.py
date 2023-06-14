# How to remove Nth occurance of word from a list

l=["darshan","suresh","darshan"]
word="darshan"
n=2

count=0

for i in range(0,len(l)):
    if l[i]==word:
        count=count+1
        if count==n:
            del l[i]

print(l)


# search an element in list
la=[3,4,5,8,9,1]
print(la[2:])

# reverse a list
p=[5,8,11,19,21]
p.reverse()
print(p)

