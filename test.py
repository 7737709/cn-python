import time #Allows you to use the time.sleep(seconds) function to pause the terminal from doing any operation for a number of seconds

print("ASCII TITLESCREEN GOES HERE")

time.sleep(2) #terminal sleeps for 2 seconds

print("\nYou awake in your plane seat") 
#Plus any more intro text you may want

def main():
    choiceinputted = False #Checks if you've inputted a value into the terminal yet to make a choice. You want this to be FAlSE to begin with

	while(choiceinputted == False):
		choicevalue = input("Enter your choice: ") #Allows you to type in "something" into the terminal
		
		if(choicevalue == "1"):
			#Do all the stuff you want to do if the first choice is selected

			choice1()
		

		elif(choicevalue == "2"):
			#Do all the stuff you want to do if the second choice is selected

			choice2()

		elif(choicevalue == "3"):
			#Do all the stuff you want to do if the third choice is selected
			
			choice3()

		else:
			#What you do if the numbers 1-3 haven't been selected

choiceinputted = False #Checks if you've inputted a value into the terminal yet to make a choice. You want this to be FAlSE to begin with

while(choiceinputted == False):
	choicevalue = input("Enter your choice: ") #Allows you to type in "something" into the terminal
		
	if(choicevalue == "1"):
		#Do all the stuff you want to do if the first choice is selected. Goes down to choice 1 of choice 1 hence 1_1.

		choice1_1()
		

	elif(choicevalue == "2"):
		#Do all the stuff you want to do if the second choice is selected. Goes down to choice 2 of choice 1 hence 1_2.

		choice2()

	elif(choicevalue == "3"):
		#Do all the stuff you want to do if the third choice is selected. Goes down to choice 3 of choice 1 hence 1_3.
			
		choice3()

	else:
		#What you do if the numbers 1-3 haven't been selected

main() #REALLY REALLY IMPORTANT. INITIALISES AND RUNS THE MAIN LOOP - ACTUALLY RUNS THE GAME.


		