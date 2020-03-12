'''Here input is taken as a String
Output is reverse of string[start : : end]
-1 refers to last alphabit of string.
so it starts from last and ends at '0' position '''



def name(string):
    print(string[-1::-1])
x=str(input('Enter any thing: '))
name(x)
