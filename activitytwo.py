breakfast = "frosties"
lunch = "smoked salmon sandwiches"
dinner = "mushroom blintzes"

#print ("This morning i had " + breakfast + " for my breakfast followed by some deliciouse " + lunch + " and " + dinner + " for dinner.")
#print( "This morning i had {}".format(breakfast) + " for my breakfast followed by some deliciouse {}".format(lunch) + " and {}".format(dinner) + " for dinner.")
my_string = ("This morning i had {}" + " for my breakfast followed by some deliciouse {}" + " and {}" + " for dinner.")

print (my_string.format(breakfast, lunch, dinner))