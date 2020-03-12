"""In this pgm elements of two matrices are first taken in a list using split function.
Using numpy.reshape() to reshape list elements into a square matrix.
After that two matrices are added using arithmatic operation '+' """

import numpy as np
x=int(input('Enter row or column of matrix: '))
print('Enter',x*x,' elements of matrix A with commas: ')
l=list(map(int,input().split(',')))
a=np.reshape(l,(x,x))
print('Matrix a:')
print(a)
print('Enter',x*x,' elements of matrix B with commas: ')
k=list(map(int,input().split(',')))
b=np.reshape(k,(x,x))
print('Matrix b:')
print(b)
print('Addition of Matrix : ')
print(a+b)
