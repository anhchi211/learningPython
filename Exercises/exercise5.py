#Unsurprisingly, the second exercise in this chapter discusses the task of writing to a file.
#Create a program which prompts the user for a file name "Give a file name: " and then for an input "Write something: ". 
#After this, the program writes the string given by the user to the file and reports "Wrote [input] to the file [name].". 
#When working correctly, the program prints something like this:
#Give a file name: log.txt
#Write something: Attencion, attencion. 10, 10, 22, 33, Adios.
#Wrote Attencion, attencion. 10, 10, 22, 33, Adios. to the file log.txt.*/

file_name=input("Give a file name: ")
something=input("Write something: ")
myfile=open(file_name, "w")
print("Wrote", something, "to the file", file_name)
myfile.write(something)
myfile.close()

loop=True
while loop:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
	decision=int(input("Please select one: "))
	if decision==1:
		file=open("notebook.txt","r")
		content=file.read()
		print(content)
		file.close()
	elif decision==2:
		file=open("notebook.txt","a")
		addedtext=input("Write a new note: ")
		file.write(addedtext)
		file.close()
	elif decision==3:
		file=open("notebook,txt","w")
		print("Notes deleted.")
		file.close()
	else:
		loop=False
print("Notebook shutting down, thank you.")