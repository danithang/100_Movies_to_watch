import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# gets the html file from the website and stores it in a variable called empire_web_page as a string using the
# .text method from the requests module
response = requests.get(URL)
empire_web_page = response.text

# gets BeautifulSoup object from the html file and parses it using the html.parser to help beautiful soup understand
soup = BeautifulSoup(empire_web_page, "html.parser")

# gets all the h3 tags for the class title and stores it in a list called movies and reverses the list to get the
# movies in ascending order(starting from 1)...the movies are in descending order in the html file
movies = soup.find_all(name="h3", class_="title")
movies_text = [movie.getText() for movie in movies]
movies_text.reverse()

# tries to open movies.txt file in read mode
try:
    with open("movies.txt", mode="r", encoding="utf-8") as file:
        movies = file.readlines()
# if the movies.txt file does not exist, it creates the file and writes the movies in the movies_text list to the file
except FileNotFoundError:
    with open("movies.txt", mode="w", encoding="utf-8") as file:
        for movie in movies_text:
            file.write(f"{movie}\n")
# if the movies.txt file exists, it checks if the movies in the movies_text list are in the movies.txt file and if
# they are not, it appends them to the file and if they are, it does nothing to the file and closes it
else:
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        for movie in movies_text:
            if movie not in movies:
                file.write(f"{movie}\n")

