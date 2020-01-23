space1 = "X"
space2 = "X"
space3 = "0"
space4 = ""
space5 = ""
space6 = "0"
space7 = "0"
space8 = "0"
space9 = "0"


print("\n \033[1;32;40m  |   |   ")
print(" {} | {} | {} ".format(space1, space2, space3))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {}  | {}  | {} ".format(space4, space5, space6))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space7, space8, space9))
print("   |   |   \n")

if space1 == space2 and space1 == space3:
    print ("You Won!")

elif space4 == space5 and space4 == space6:
    print ("You Won!")

elif space7 == space8 and space7 == space9:
    print ("You Won!")

elif space1 == space5 and space1 == space9:
    print ("You Won!")

elif space3 == space5 and space3 == space7:
    print ("You Won!")

elif space1 == space4 and space1 == space7:
    print ("You Won!")

elif space2 == space5 and space2 == space8:
    print ("You Won!")

elif space3 == space6 and space3 == space9:
    print ("You Won!")