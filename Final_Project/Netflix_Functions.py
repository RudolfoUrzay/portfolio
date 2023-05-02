import csv
from charts import run


# import Netflix;

def count_number_of_movies(filePath):
    num_rows = 0
    for row in open(filePath):
        num_rows += 1
    print(f"Successfully loaded {num_rows} records.")

def retrieve_movie_data(movie_name):
    with open("movies.csv") as file:
        print("Please insert movie name:")
        movie_name = input()
        file_reader = csv.reader(file)
        for values in file_reader:
            movie_base = values[1]
            if movie_name == movie_base:
                print(values)
                run()

def retrieve_movie_year(movie_year):
    with open("movies.csv") as file:
        movie_year = input(int())
        file_reader = csv.reader(file)
        for values in file_reader:
            year = values[3]
            if movie_year == year:
                print(values)
                run()


def retrieve_actors_name(actors_name):
    with open("movies.csv") as file:
        print("Insert the name of the Actors: ")
        actors_name = input()
        file_reader = csv.reader(file)
        for values in file_reader:
            name_base = values[6]
            if actors_name == name_base:
                print(values)
                run()


def retrieve_movie_rating(country):
    with open("movies.csv") as file:
        print("Insert Country: ")
        country = input()
        file_reader = csv.reader(file)
        for values in file_reader:
            country_base = values[7]
            if country == country_base:
                movie_ranking = values[8]
                ranking = str(7.0)
                if movie_ranking >= ranking:
                    print(values[1])
                    run()
