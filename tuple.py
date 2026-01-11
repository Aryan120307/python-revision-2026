#tuple - it is also used to store different types of data
# it is represented by ()
#it is ordered and allows duplication
t=(1,2,3,'aryan','amar',1)
print(t)
#methods 
#count() - it will count the frequency of a particular element in the tuple 
tu=(1,2,2,2,3,4,4,5,6,)
print(tu.count(2))
#index() - it will give you the index number of the element 
print(tu.index(2))
#string -text data or array of character 
# it follows indexing and slicing 
name='aryan sharma'
#space also contain a slice
print(name[:5])
#methods in string
#upper() - it will convert all the character to uppercase
print(name.upper())
txt='hello'
txt=txt[0].upper()+txt[1:]
print(txt)
#lower - it will convert all the character to lowercase
print(name.lower())
#capitalize() - it will convert the first character to uppercase 
print(name.capitalize())
#title() - it will capitalize all the first character of each word in the string
text='into to pyhton'
print(text.title())
#strip()- it will remove the extra space from the start and the end of the string 
nam='   abc  '
print(nam.strip())
#replace() - it will remove in btw space also
texte='h  e  l  l  o'
texte=texte.replace("","")
print(texte)
# input()- it is used to take input form the user 
namess=input("enter your name :")
print(namess)



