import csv
import Netflix_Functions

from Netflix_Functions import count_number_of_movies
from Netflix_Functions import retrieve_movie_data
from Netflix_Functions import retrieve_movie_year
from Netflix_Functions import retrieve_actors_name
from Netflix_Functions import retrieve_movie_rating

print("\n")

file_path = "movies.csv"
file = open(file_path)
file.read()

count_number_of_movies(file_path)

print("\n")

print("Select a number from below: \n"
      "1º - Retrieve the details for a specific movie, \n"
      "2º - Retrieve the details for movies released in a specific year \n"
      "3º - Retrieve the details for movies that star a particular cast \n"
      "4º - Retrieve the top movies by rating for a specific country \n")

option = input()

if int(option) == 1:
    retrieve_movie_data(file_path)
elif int(option) == 2:
    print("Insert the year:")
    retrieve_movie_year(file_path)
elif int(option) == 3:
    retrieve_actors_name(file_path)
elif int(option) == 4:
    retrieve_movie_rating(file_path)
else:
    print("Could not find the option!!!")
