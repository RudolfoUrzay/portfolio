import csv;
import Netflix_Functions;

from Netflix_Functions import read_file
from Netflix_Functions import retrieve_data
from Netflix_Functions import retrieve_movie_year
from Netflix_Functions import retrieve_actors_name
from Netflix_Functions import retrieve_movie_rating

file_path = open("movies.csv")
read_file()

print("Select a number from below: "
      "1º - Retrieve the details for a specific movie, "
      "2º - Retrieve the details for movies released in a specific year"
      "3º - Retrieve the details for movies that star a particular actor"
      "4º - Retrieve the top movies by rating for a specific country")

option = input(int())

try:
    if option == 1:
        retrieve_data()
    elif option == 2:
        print("Insert the year:")
        retrieve_movie_year()
    elif option == 3:
        print("Insert the name of the Actor: ")
        retrieve_actors_name()
    elif option == 4:
        print("Insert Rating: ")
        retrieve_movie_rating()

except IOError:
    print("Could not read the file")

name_search = input(print("Please insert movie id:"))

