import api
import requests.exceptions
import logbook
import sys


app_log = logbook.Logger('App')


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
        app_log.trace(f'Search successful: keyword: {keyword}, {len(results)} results')
    except requests.exceptions.ConnectionError:
        msg = "Could not find server. Check your network connection."
        print(f'ERROR: {msg}')
        app_log.warn(msg)
    except ValueError:
        msg = "You must specify a search term."
        print(f'ERROR: {msg}')
        app_log.warn(msg)
    except Exception as x:
        msg = f'Oh that didn\'t work!: {x}'
        print(f'{msg}')
        app_log.exception(x)



def init_logging(filename: str=None):
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level).push_application()

    msg = f'Logging initiated, level: {level}, mode: {"stdout mode" if not filename else "file mode: " + filename}'
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging('movie-app.log')
    main()
