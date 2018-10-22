from typing import List

import requests
import collections
import random
import logbook
import time

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


api_log = logbook.Logger('API')

def find_movie_by_title(keyword: str) -> List[Movie]:
    t0 = time.time()
    if keyword == '':
        api_log.trace(f'Starting search with no keyword')
    else:
        api_log.trace(f'Starting search for \'{keyword}\'')
    if not keyword or not keyword.strip():
        api_log.warn("No keyword supplied")
        raise ValueError('Must specify a search term.')

    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    api_log.trace(f'Request finished, status code {resp.status_code}')
    resp.raise_for_status()

    results = resp.json()
    results = create_random_errors(results)

    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    t1 = time.time()
    api_log.trace(f'Finished search for {keyword}, {len(movies)} results in {int(1000*(t1-t0))} ms')
    return movies


def create_random_errors(results):
    # This is a method to occasionally create some more
    # interesting errors other than simply network connectivity errors
    # which are the only "real" errors. This will let us test
    # more types.

    num = random.randint(1, 20)
    if 16 < num <= 18:
        return {}  # Whoops! No data.
    elif 18 < num <= 20:
        raise StopIteration()

    return results  # no errors here.
