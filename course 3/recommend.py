import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    api = "https://tastedive.com/api/similar"
    d = {'q': movie, 'type': 'movies', 'limit': 5}
    res = requests_with_caching.get(api, params = d)
    return res.json()

def extract_movie_titles(dic):
    lst = []
    for movie in dic["Similar"]["Results"]:
        lst.append(movie["Name"])
    return lst

def get_related_titles(lst):
    output = []
    for name in lst:
        movies_dic = get_movies_from_tastedive(name)
        titles = extract_movie_titles(movies_dic)
        for title in titles:
            if title not in output:
                output.append(title)
    return output

def get_movie_data(movie):
    api = "http://www.omdbapi.com/"
    d = {'t': movie, 'r': 'json'}
    res = requests_with_caching.get(api, params = d)
    return res.json()

def get_movie_rating(dic):
    for source in dic['Ratings']:
        if source['Source'] == 'Rotten Tomatoes':
            return int(source["Value"][:-1])
    return 0

def get_sorted_recommendations(lst):
    output = get_related_titles(lst)
    rating = {}
    for movie in output:
        rating[movie] = get_movie_rating(get_movie_data(movie))
    sort_out = sorted(output, key=lambda movie: (rating[movie], movie), reverse = True)
    return sort_out
