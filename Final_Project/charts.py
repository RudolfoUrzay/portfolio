import matplotlib.pyplot as plt
import csv

def run():
    # Best rating movies from 2010 to 2020
    movie_rating = []
    movie_names = []

    with open('movies.csv') as file:
        file_reader = csv.reader(file)
        for values in file_reader:
            year_movie = values[3]
            movie_rating.sort()
            rating_movie = values[8]
            movie_country = values[7]
            if '2010' <= year_movie <= '2020':
                if '7' <= rating_movie <= '9':
                    if movie_country == 'Spain':
                        movie_rating.append(values[8])
                        movie_names.append(values[1])

    # How many movies have been released every year from 2010

    movie_count = []
    year_count = []

    with open('movies.csv') as file:
        file_reader = csv.reader(file)
        for values in file_reader:
            year = values[3]
            movies = values[1]
            year_count.sort()
            if year >= '2010':
                year_count.append(values[3])
                movie_count.append(movies)

    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)

    #ax1.title('Best Ratings from 2010 to 2020 in Spain')
    ax1.barh(movie_names, movie_rating)
    #ax1.title("Best Ratings from 2010 to 2020 in Spain")
    ax1.set_ylabel("Movie Name")
    ax1.set_xlabel("Rating")

    ax2 = fig.add_subplot(1, 2, 2)

    ax2.bar(year_count, movie_count)
    # ax2.title("How many movies have been released every year from 2010")
    ax2.set_ylabel("Quantity of Movies")
    ax2.set_xlabel("Year")
    ax2.axes.yaxis.set_ticklabels([])
    #ax2.axes.get_yaxis().set_visible(False)


    #plt.tight_layout()

    plt.show()

run()








