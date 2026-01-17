import numpy as np
#    1)create a numpy array with random integer in range 10 to 100
#       b) the sample size and the no of size should be 25
#       c) after this give me all the unique elements in the array 
a=np.random.randint(10,100,25)
print(a)
ar=np.unique(a)
print(ar)
print(ar.shape)
#    to find random no we use seed() to fix value above topline
se=np.random.seed()
print(se)
#   2) dice=[1,2,3,4,5,6] everytime i run the codde , i want a random value from the dice?
import random
dice=[1,2,3,4,5,6]
roll=random.choice(dice)
print(roll)
#   3)create a numpy array with shape 2*3 with random integer in range from 0 to 100?
#   a)reshape the array with  shape 3*2 & print the updated shape of array 
x=np.random.randint(0,100,(2,3))
print(x)
x=x.reshape(3,2)
print(x)
#   4) create 5*5 matrix , fil it with random integer in range 0 to 100 
#   a) replace all values greater than 50 with 290 , print modified array
x=np.random.randint(0,100,(5,5))
print(x)
x[x>50]=290
print(x)
#   5) create a numpy array of no  from  1-20 use arange function
#       a) do extract even no ?
ar=np.arange(1,21)
print(ar)
ar=np.arange(1,21,2)
print(ar)
#or 
even=ar[ar%2==0]
print(even)
#   6) arr=[10,20,30,40,50]
#       a) insert 100 btw every two elements?
#   7) create a random array ,range from 0-100 , size=50?
#       a) print 1st 10 elements ?
#       b) print last 10 elements using +ve indexing 
#       c) print the last 10 element using -ve indexing 
#       d) print element from index 10 to 20
#       e) print element at index 25
#       f) print entire array using -ve indexing 
arr=np.random.randint(0,100,size=50)
print(arr)
arr[0:10]
arr[40:50]
arr[-10:]
print(arr[25])
arr[-50:]