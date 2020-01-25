from topNews import return_headlines
from topNews import return_numHeadlinesMod
from topMovies import get_topMod
import os
import time

url_Movie = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth'
url_MostPopular = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'
url_Mtest = 'https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter'

# Formats the link appropriately
def format(url = url_Movie, num_Movies = 5, headline_category = 'business', num_Headlines = 5):
    output = return_numHeadlinesMod('business', num_Headlines)
    return output

# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t])))

# Main method - sends notifications through terminal in 45 second interval
if __name__ == "__main__":
    newsList = format()
    movieList = get_topMod(url_Movie, 5)
    for i in range(len(newsList)):
        output = newsList[i] + 'Top Movie: ' + movieList[i]
        notify(title = 'NEWS UPDATE', message = str(output))
        time.sleep(45)
