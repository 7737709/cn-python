
def choice_3():
    print ("What would you like to do?")
    decide = input ("You can either 1) head to the galley and try and get a weapon or 2) Motion to the steward to try and comunicate and plan something?\n")
    if decide == "1":
        print ("Your seat is situated right by the galley and you succesfully get a hold of a weapon.")
    elif decide == "2":
        print ("There's no stewards near you and there is nothing for you to do.\n The plane continues on to the unknown destination and your gone forever! ")

def choice_1():
    print("Try another door.")
    choices = input ("What door would you like to try next? 1) Lavatory or 2) Business Class? \n")
    if choices == "1":
        print ("You've found the bomb") 
    elif choices == "2":
        print ("You walk right into the hijackers and are neutrolised!\nGame Ended")

def choice_2():
    print("If you want to be a steward you have to find a set of clothes quickly")
    decision = input ("Where would you like to try first? 1) Galley 2) In the floor Where the saftey demonstation equipment is kept?\n")
    if decision == "1":
        print ("The stewards shove you back in your seat.")
    elif decision == "2":
        print ("Well done, you've found a spare set of arline uniform.\n")

choice = input ("What do you want to be? \n 1) Pilot \n 2) Steward \n 3) passenger \n")

if choice == "1":
    print("There's nothing you can do as the cockpit door has to stay closed as of protocol!")
    # choice_1 = input("What is going to happen?")
    choice_1()

elif choice == "2":
    print ("Are you going to listen to the hijackers or are you going to try and fight forward?")
    choice_2()

elif choice == "3":
    print ("You are situated right in the back of the plane!")
    choice_3()
else:
    print("Please input a valid number.")
