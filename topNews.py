#Google NewsApi was used, documentation found here: https://newsapi.org/docs/endpoints/top-headlines

from newsapi import NewsApiClient
from urllib import request
import json 

news_url = ''

# This function prints news headlines from given category
def print_headlines(category): 
    news_url = 'https://newsapi.org/v2/top-headlines?category=' + category + '&country=us&apiKey=40ac3cd1f8344ea19a5bd055f75ba17c'
    request_obj = request.urlopen(news_url)
    top_head = json.load(request_obj)
    for i in top_head['articles']:
        print('NEWS: ', i['title'])
        print('Description: ', i['description'])
        print('')

# This function returns the headlines from a given category
def return_headlines(category):
    output = ''
    news_url = 'https://newsapi.org/v2/top-headlines?category=' + category + '&country=us&apiKey=40ac3cd1f8344ea19a5bd055f75ba17c'
    request_obj = request.urlopen(news_url)
    top_head = json.load(request_obj)
    for i in top_head['articles']:
        title = str(i['title'])
        output += (get_source(title) + ': ' + title[0 : index_end(title) - 1] + '\n')
        output += ('Description: ' + str(i['description']) + '\n')
        output += ('\n')
    return output

# This function returns a specified number of headlines
def return_numHeadlines(category, topNum):
    output = ''
    news_url = 'https://newsapi.org/v2/top-headlines?category=' + category + '&country=us&apiKey=40ac3cd1f8344ea19a5bd055f75ba17c'
    request_obj = request.urlopen(news_url)
    top_head = json.load(request_obj)
    j = 0
    for i in top_head['articles']:
        if j < topNum:
            title = str(i['title'])
            output += (get_source(title) + ': ' + title[0 : index_end(title) - 1] + '\n')
            output += ('Description: ' + str(i['description']) + '\n')
            output += ('\n')
            j += 1
    return output

# This function returns the top 'topNum' number of headlines in the most readable manner
def return_numHeadlinesMod(category, topNum):
    output = ''
    output_list = []
    news_url = 'https://newsapi.org/v2/top-headlines?category=' + category + '&country=us&apiKey=40ac3cd1f8344ea19a5bd055f75ba17c'
    request_obj = request.urlopen(news_url)
    top_head = json.load(request_obj)
    j = 0
    for i in top_head['articles']:
        if j < topNum:
            title = str(i['title'])
            output += (get_source(title) + ': ' + title[0 : index_end(title) - 1] + ' --> ')
            output += (str(i['description']))
            if j != topNum - 1: output += ' || '
            output_list.append(output)
            j += 1
            output = ''
    return output_list

# This function returns the source of a given unformatted title
def get_source(title):
    ind = index_end(title)
    return str(title[ind + 2 : len(title)])

# This function returns the end index of a title in an unformatted title string
def index_end(title):
    for i in range(len(title) - 1, 0, -1):
        if title[i] == '-': return i
    else: return 0

# Main
if __name__ == "__main__":
    x = input("Pick a category of news (business, entertainment, general, health, science, sports, technology: ")
    print(return_numHeadlines(x, 10))
