#list- list is the collection of elements of different datatypes
# it is represented by []
# in list we have indexing
# it is ordered and allowed duplicates 
basket=['apple','banana','grape',5,6,7]
print(basket)
#indexing- it is used to access the particular elements in the list
#indexing starts from 0
li=[10,20,30,40,50,60]
print(li)
print(li[1])
#indexing starts from 0
#-ve indexing  starts from -1
print(li[-1])
# to reverse the list or to know the last element of the list we use -1 index
#slicing - it is used to acces the part of list 
#[start index : end index]
print(li[1:4])
#end index is not included in slicing 
li1=[10,20,30,40,50,60]
print(li[1:5])
# for -ve indexing 
print(li[-5:-1])
#we can skip start index if we already if we already starting from 0th index
print(li[:4])
# if you want to go till last you can skip  end index
print(li[2:])
#full list
print(li[:])
# to skip the elements using step sizes 
print(li[::2])
print(li[::4])

#print even no 
lis=[1,2,3,4,5,6,7,8,9,10]
print(lis[1::2])
#print odd no
print(lis[::2])
#methods in list
#len() - it will give us the length of the list 
print(len(lis))
#append()- it will add the element at the end of the list 
lis.append(11)
print(lis)
#insert()- it will insert the element at the specific index 
lis.insert(0,0)
print(lis)
#remove() - it will remove the specific element from the list 
lis.remove(11)
print(lis)
# if want to change or update a specific element at the specific index in the list
lis[2]=30
print(li)
#pop()-it will remove the last element from the list or can by the index also
lis.pop()
print(li)
#index() - it will give us the index of the specific element
lis.index(30)
