""" imports fresh_tomatoes tells the program to use the content of fresh_tomatoes """
import fresh_tomatoes
""" import media tells the program to use the content of import media """
import media

""" toy_story is an instance variable of class Movie it is the details that class Movie initializes """
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.dvdsreleasedates.com/posters/800/T/Toy-Story-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.coolshite.net/wp-content/uploads/2009/12/Avatar-Poster.jpeg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print (avatar.storyline)                                             
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Kids who can rock",
                             "http://images.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                          "A rat that can cook",
                          "https://www.movieposter.com/posters/archive/main/50/MPW-25274",
                          "https://www.youtube.com/watch?v=FAfR8omt-CY")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "A midnight in Paris",
                                "http://www.movieposter.com/posters/archive/main/145/MPW-72510",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("The Hunger Games",
                           "Fighting for food",
                           "http://ricmeyers.com/wp-content/ric-meyers-uploads/2012/03/the-hunger-games-movie-poster-24.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")
wreck_it_ralph = media.Movie("Wreck-it Ralph",
                             "A video game movie",
                             "http://ca.movieposter.com/posters/archive/main/157/MPW-78849",
                             "https://www.youtube.com/watch?v=87E6N7ToCxs")
""" an array of movies for the function def open_movies_page from fresh_tomatoes.py to open """
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, wreck_it_ralph]
""" Calls the open_movies_page function from fresh_tomatoes.py to create movie website """
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
