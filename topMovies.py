import re
import requests
from bs4 import BeautifulSoup as BSoup

API_KEY = 'E38B4AEDMKBGQPFM'
url_Movie = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth' # will be used for web scraping
url_MostPopular = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'
url_Mtest = 'https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter'

#EDITS: instead of making the movies make them a dictionary where the name correlates to its rating -- imbd site has rating between
# the tags "<strong>"

def title_return(url):
    # response = requests.get(url_Movie)
    movie_Data = requests.get(url).text
    soup = BSoup(movie_Data, 'lxml')
    movie_Title = soup.find_all('a', attrs = {'href' : re.compile(r'\/title\/tt+\d*\/')})
    return movie_Title

def parse_title(url):
    new_title = title_return(url)
    title_list = []
    for i in new_title: 
        chunk = str(i).split('>')
        if(len(chunk) <= 3):
            if str(chunk[1][0 : 1]).isspace():
                title_list.append(chunk[1][1:len(chunk[1]) - 3])
            else: title_list.append(chunk[1][0:len(chunk[1]) - 3])
    return title_list

def get_top(url, num): # for errors: catch an error if 'num' is too long; it exceeds the number of movies on the site
    new_parse = parse_title(url)
    top_list = []
    if str(new_parse[2]) == 'Get Tickets':
        for i in range(1, num * 2):
            if str(new_parse[i]) == 'Get Tickets': continue
            top_list.append(new_parse[i])
    else: 
        for i in range(1, num + 1):
            top_list.append(new_parse[i])
    return top_list

def get_topMod(url, num): # for errors: catch an error if 'num' is too long; it exceeds the number of movies on the site
    new_parse = parse_title(url)
    top_list = []
    if str(new_parse[2]) == 'Get Tickets':
        for i in range(1, num * 2):
            if str(new_parse[i]) == 'Get Tickets': continue
            top_list.append(new_parse[i])
    else: 
        for i in range(1, num + 1):
            top_list.append(new_parse[i])
    return top_list

if __name__ == "__main__":
    print('CLEAR MARKER: TOP 20 POPULAR MOVIES OUT NOW ')
    for i in get_top(url_MostPopular, 10):
        print(i)
    print('\nCLEAR MARKER: TOP 20 LATEST MOVIES ')
    for i in get_top(url_Movie, 10):
        print(i)