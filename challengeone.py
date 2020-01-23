time = 1645
place_of_work = "highview"
town_of_home = "manchester"
travel = "commuting"

if time > 1830:
    print ("I am in {}".format(town_of_home))

elif time > 1800:
    print ("I am {}".format(travel))

elif time > 900:
    print ("I am at {}".format(place_of_work))
    
elif time > 800:
    print ("I am {}".format(travel))

elif time < 700:
    print ("I am in {}".format(town_of_home))