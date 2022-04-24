
import random

userinput = input('What is your name?: ')
greeting= "Hello " + userinput + " your lucky number is: " + str(random.randint(1,10))

print(greeting)