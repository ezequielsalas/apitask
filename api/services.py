from datetime import datetime as dt
import requests

API_BASE_URL = 'https://www.anapioficeandfire.com/api'


def get_books(params):
    url = API_BASE_URL + '/books'
    r = requests.get(url, params)
    books = r.json()

    incoming_date_format = '%Y-%m-%dT%H:%M:%S'
    date_format = '%Y-%m-%d'

    books_list = [{
            "name": b['name'],
            "isbn": b['isbn'],
            "authors": b['authors'],
            "number_of_pages": b['numberOfPages'],
            "publisher": b['publisher'],
            "country": b['country'],
            "release_date": dt.strptime(b.get('released', ''), incoming_date_format).strftime(date_format),
        } for b in books]

    return books_list
