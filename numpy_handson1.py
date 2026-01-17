import numpy as np 
#   1)create two numpy array with datatype int & float? [1,2,3,4,5,6]
#       a)print the array 
#       b)know the datatype
a=np.array([1,2,3,4,5,6],dtype=int)
print(a)
b=np.array([1,2,3,4,5,6],dtype=float)
print(a)
print(a.dtype)
print(b.dtype)
#   2)a. create numpy array having dimension of zero,one.two ,three ?
#     b. print the shape and dimension of two array ?
a0=np.array([1])
a1=np.array([1,2,3])
a2=np.array([[1,2],[3,4]])
a3=np.array([[1,2],[3,4],[5,6]])
print(a1.shape)
print(a1.ndim)
print(a0.shape)
print(a0.ndim)
print(a2.shape)
print(a2.ndim)
print(a3.shape)
print(a3.ndim)
#   3) create 2*2,3*3,4*4,4*6 identity matrix using numpy 
two=np.identity(2)
print(two)
three=np.identity(3)
print(three)
four=np.identity(4)
print(four)
x=np.eye(4,6)
print(x)
#eye by default gives the output as float
# 4) create an array bwith shape (2,5) and all the elementsshould be zero ?
a=np.zeros((2,5),dtype='int')
print(a)
#   5) create a numpy array with shape 3*5 and all elements should be 55?
b=np.ones((3,5),dtype='int')*55
#or by second ,method to print 55
x=np.full((3,5),55)
print(x)




