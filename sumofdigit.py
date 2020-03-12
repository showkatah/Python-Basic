def sum(x):
    '''while(x!=0):  #General Method
        r=x%10
        s=s+r
        x=x/10
    return int(s)'''
    return 0 if x==0 else int(x%10) + sum(x/10)  #recursive method
x=int(input('Entr any integer: '))
print('sum of digits: ',sum(x))
