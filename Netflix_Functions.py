import csv;
#import Netflix;

def read_file(record, headings):
    records = 0
    with open("movies.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for line in csv_reader:
            records.append(line)
            print("Done!")
            print(f"Successfully loaded {len(records)} records.")

def retrieve_data(movie_name, movie_base, name_search):
    with open("movies.csv") as file:
        movie_name = input()
        file_reader = csv.reader(file)
        for values in file_reader:
            movie_base = values[1]
            if movie_name == movie_base:
                name_search = range(len(movie_base))
                print(f"Successfully loaded {len(name_search)} records.")

def retrieve_movie_year(movie_year, num_year, year):
    with open("movies.csv") as file:
        movie_year = input(int())
        num_year = 0
        file_reader = csv.reader(file)
        for values in file_reader:
            year = int(values[3])
            if movie_year == year:
                num_year += 1
                print(f"{values[1]},{values[2]},{values[4]},{values[5]}")


 def retrieve_actors_name(actors_name, name_base):
    with open("movies.csv") as file:
        actors_name = input()
        file_reader = csv.reader(file)
        for values in file_reader:
            name_base = values[6]
            if actors_name == range(len(name_base)):
                print(f"{values[1]}, {values[2]}, {values[3]}, {values[4]}, {values[5]}")

def retrieve_movie_rating ():
    with open("movies.csv") as file:
        movie_rating = input(float())
        file_reader = csv.reader(file)
        for values in file_reader:
            rating_base = values[8]
            if movie_rating ==  rating_base:
                print(movie_rating)
