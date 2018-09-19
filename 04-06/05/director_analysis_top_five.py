import csv
from collections import defaultdict
from collections import namedtuple
from collections import Counter

DATAFILE = 'movie_metadata.csv'

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=DATAFILE):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()
print(directors)

myCount  = Counter()
for director, movies in directors.items():
	myCount[director] += len(movies)
	print(f'myCount[{director}] - {myCount[director]}')

print(myCount.most_common(5))