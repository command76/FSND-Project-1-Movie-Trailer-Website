""" imports the webbrowser module from the python standard library """
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    """ initializes and creates space in memory to remember details about movies"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """ this function is an instance method because it is associated with an instance variable.
    It opens a web browser and plays a trailer of the movie """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
