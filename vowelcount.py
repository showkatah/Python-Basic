x=str(input('Enter '))
l=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in x:
    for j in l:
        if i==j:
            c=c+1
print(c)
