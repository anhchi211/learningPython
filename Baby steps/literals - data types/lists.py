
# List with three items [42, 3.14, 'hello']
# List with one item [100]
# Empty list []

#Create a list: list('haha') -> ['h', 'a', 'h', 'a']

#replace literals in a list
list= ['green', 'blue']
#index    0        1   
list[1]= 'green' 
print(list) 

#Notes: While tuples and lists both store sequences of data, they have a few distinctions.
#Whereas you can change the values in a list, the values inside a tuple cannot be changed. 
#Also, tuples are stored within parenthesis whereas lists are declared between square brackets.
#For example: liste = ('green', 'blue') -> this is a tuple, the value inside cannot be changed.
#Fix: as_list= list (liste) 

#list.append(): adds a single item to the existing list
list= ['green', 'blue']
list.append ('red')
print(list)

#list.insert(): inserts a given element at a given index in a list
list.insert(0, 'pink') 
print(list)

#list.clear(): removes all the elements from a list

#list.pop(): removes an item at the specified index from the list & without mentioning the index value -> remove the last element
list.pop()
print(list)

#list.remove(): remove the specific value in the list
list.remove('green')
print(list)

#list.index(): print out the postion of the value in the list
index=list.index('pink')
print(index)

#copy list . when you change the values of list2 it does not affect list
list2=list.copy()
print(list2)

# list2 = list -> when you change the values of list2 it affects list 









