#coffee_is_grinding = True

#def press_grind_beans():
#    if coffee_is_grinding:
#        print("The coffee is grinding")
#    else:
#        print("The coffee is not grinding")
#
#press_grind_beans()

def coffee_order(size,type_of_drink):
    print("I want a {} {}".format(size,type_of_drink))

coffee_order("Large", "Mocha")
coffee_order("Small", "Cocco")
coffee_order("Medium", "Latte")