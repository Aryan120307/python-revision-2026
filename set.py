#set - set is the collection of unique elements 
# we user {} to represent a set 
#in set we dont have key , we just have values
#syntax for set
# set_name={value1, value2, value3,value4..}
s1={1,2,3,'aryan','amar','guru',9,5}
print(s1)
# set does not follow anyorder , duplicate values are not allowed in set 
s2={1,2,3,4,'aryan','guru','amar',1,2,7,6,'ayush'}
print(s2)
#we cant update in sets
#add()
s1.add(30)
print(s1)
#remove()
s1.remove('amar')
print(s1)
#union()- it will give us all the elements from both the set without duplicacy
s3={1,2,3,4}
s4={4,5,6,7,8,}
print(s3.union(s4))
#intersection() - it will give you the common elements from both the sets
print(s3.intersection(s4))
#difference () - it will give you the elements which are present in first set but not in second set
print(s3.difference(s4))
#problems with set
#1. unordered , cant access specific values , duplicate are not allowed .
# unordered , cant access specific values ,duplicates are not allowed 
