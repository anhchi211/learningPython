# The first exercise in the fourth chapter is a basic while-iteration. 
# The assignment is simple: create a program which on each turn prints the round number. 
# Start by the round number 0 and make the iteration continue for four loops. 


totallap=4
nowlap=0
while nowlap<=totallap:
	print("This is lap", nowlap)
	nowlap+=1


# Create a program which, for every loop, prompts the user for input, and then prints it on the screen. 
# If the user inputs the string "quit", the program prints "Bye bye!" and shuts down.

loop=True
while loop:
	userwrote=input("Write something: ")
	if userwrote=="quit":
		print("Bye bye!")
		loop=False
	else:
		print(userwrote)


# The third progam tests a for-iteration. In this program, build a calculator, which asks the user for a number,
#  and calculates the sum of all positive numbers from 0 to the usergiven input. If the user gives the number 4, 
#  the program calculates the sum 0+1+2+3, if 7, the calculation is 0+1+2+3+4+5+6. Finally, the program produces an answer with the printout "The sum was:" and an answer.

number=int(input("Give a number: "))
result=t=i=0
while i<number:
	result+=i
	i+=1
print("The sum was: ", result)


# The last exercise in this chapter continues with the exercise from the last chapter, the calculator. 
# In this exercise, expand the existing code by implementing the following new features:
# (A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. 
# The user has to select "6" in the menu to exit the program. (B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input.
# By selecting "5" in the calculator menu, the user can change the given numbers. 

print("Calculator")
number1=int(input("Give the first number: "))
number2=int(input("Give the second number: "))
print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit\nCurrent numbers: ", number1, number2,)
number3=int(input("Please select something (1-6): "))
while number3!=6:
	if number3==1:
		print("The result is: ", number1+number2)			
	elif number3==2:
		print("The result is: ", number1-number2)
	elif number3==3:
		print("The result is: ", number1*number2)
	elif number3==4:
		print("The result is: ", number1/number2)
	elif number3==5:
		number1=int(input("Give the first number: "))
		number2=int(input("Give the second number: "))
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit\nCurrent numbers: ", number1, number2,)
	number3=int(input("Please select something (1-6): "))
print("Thank you!")



