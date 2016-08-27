# Udacity FSND Project One
## Movie Trailer Website
### Description
Build a website of your favorite movies that previews the movie trailer, poster image, title and description of your favorite movies.

### How it works
The data used for the movie trailer website is saved in two separate python files __media.py__ and __entertainment_center.py__ that data is then used by a third python file that extracts data from a list or an array and uses that data to create a movie trailer website.

*This class provides a way to store movie related information:*

`class Movie():`

*This initializes and creates space in memory to remember details about movies:*

`def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube`

*This function is an instance method because it is associated with the class Movie instance variables. It opens a web browser and plays a trailer of the instance veriables movie:*

`def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)`

*Tells the program to use the content of **fresh_tomatoes.py:***

`import fresh_tomatoes`

*Tells the program to use the content of **media.py**:*

`import media`

*This is an instance variable of class Movie it is the details that class Movie initializes:*

`toy_story = media.Movie("movies title",
                        "description of movie",
                        "link to poster image",
                        "link to movie trailer website")`

*This is an array of movies for the function `def open_movies_page` from **fresh_tomatoes.py** to open:*

`movies = [movie1, movie2, movie3, movie4, movie5, movie6, movie7]`

*This line calls the open_movies_page function from **fresh_tomatoes.py** to create a movie website:*

`fresh_tomatoes.open_movies_page(movies)`

### Credit
[adarsh0806](https://github.com/adarsh0806) for providing Udacity starter code for fresh_tomatoes.py.
[Udacity](https://www.udacity.com) for providing instructions on how to construct the movie trailor website.
