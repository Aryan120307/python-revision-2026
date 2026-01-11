# dictionary - dictionary like sets are unordered collection of data but they store key value pairs i.e two associated value 
#dict_name={'key1': value1,'key2':value2,'key3':value3,'key4':value4}
person={'name':'aryan','age':18,'city':'faridabad','country':'india'}
print(person)
#if i want to check a specific detail of the person 
#city of the person
print(person['city'])
print(person['name'])
# if i want to change a specific detail of the person
person['age']=19
print(person['age'])
# if i want to add a new key value pair  to the dictionary 
person['salary']=50000
print(person['salary'])
# if i want to remove or delete a specific key value pair from the dictionary 
del person['country']
print(person)
#mutable data type - if i can do any changes like add,delet,update after the creation  , the those data tyoes are called to be mutable data types
#eg - dictionary ,list ,set etc
#immutable data type - if i cant do any changes like add delete or update after creation , then those data types are called to be immutable data types eg 
# eg - tuple 
# #methods in dictionary 
# key()-it will give us all the keys present in the dictionary . 
print(person.keys()) 
# values() - it will give us all the values present in the dictionary
print(person.values())
# items()- it will give us all the key value pairs present in the dictionary together in a tuple method
print(person.items())