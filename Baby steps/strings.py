# Blacklash (\) character rules for string
   # (\) use as the last character of a line -> indicate the next line is a continuation
   # (\n\) (\n) use as the last character of a line -> to make the string contain two lines

myname = "Nguyen Diep \nAnh Chi"
print(myname) 

mylastname = "Nguyen"
myname = " Diep Anh Chi"
print(mylastname + myname)

myfullname = mylastname + myname
print (myfullname)

# upper & lower function 
print (myfullname.upper())
print (myfullname.lower())

# to check if the string is upper or lower. Output -> True or False
print (myfullname.islower()) 
print (myfullname.isupper())

#len function -> How many characters included in the string?
print(len(myfullname))

#replace function
print(myfullname.replace("Nguyen", "Do"))







