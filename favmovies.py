fav_movies=[
    "fauda", 
    "jumanji",
    "money heist"
]

fav_movies.insert(1, "another")
fav_movies.append("test")

for movie_index in fav_movies:
    print (movie_index)

def film_check():
    if fav_movies[3] == "money heist":
        print ("yes it's money heist")
    else:
        print ("boo we want money hesit")

film_check()
3

