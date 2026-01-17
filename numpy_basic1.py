import numpy as np
#create the array
a=np.array([1,2,3,4])
print(a)
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
o=np.ones((3,4),dtype=int)
print(o)
o=np.zeros((3,4),dtype=int)
print(o)
o=np.ones((3,4),dtype=int)*3
print(o)
# random floating number btw a range of 10 to 100
r=np.random.randint(0,10,(3,4))
print(r)
r=np.random.randint(0,10)
print(r)
# r=low+(high-low) * np.random.rand()
r=10+(100-10)*np.random.random((3,3))
print(r)
# arange - start,end , step
ar=np.arange(10,20,1)
print(ar)
# btw specific range,considering start ,end and equal gap btw no 
li=np.linspace(10,100,13)
print(li)
#ARRAY INSPECTION
o=np.array([[3,3,3,3],[3,3,3,3],[3,3,3,3]])
print(o)
print(o.shape)
print(o.size)
print(o.ndim)
print(o.dtype)
#modifying the shape
o.shape=(3,4)
o=o.reshape(12,1)
print(o)
#maths function
print(np.sqrt(o))
print(np.mean(o))
print(np.median(o))
print(np.std(o))
print(np.power(o,2))
r=np.random.randint(10,100,(4,4))
print(r)
o=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#indexing and slicing 
print(r[0][1])
#[start:stop:step]
print(r[2::,2::])#1st -rows then columns 
print(r[1::2,-1::-2])
#numpy 3rd module
print(np.sum([[1,2,],[3,4,]]))
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.add(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.subtract(a,b))
#stack
r=np.stack((a,b))
print(r)
print(np.equal(a,b))
#hstack-horizontal stack
print(np.hstack((a,b)))
#vstack -vertical stack
print(np.vstack((a,b)))
#column stack
print(np.column_stack((a,b)))






