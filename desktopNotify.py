# import os
# import pync

# pync.notify('Hello World')
# pync.notify('Hello World', title='Python')
# pync.notify('Hello World', group=os.getpid())
# pync.notify('Hello World', activate='com.apple.Safari')
# pync.notify('Hello World', open='http://github.com/')
# pync.notify('Hello World', execute='say "OMG"')
# pync.notify('')

from topNews import return_headlines
from topNews import return_numHeadlinesMod
from topMovies import get_topMod
import os
import time

url_Movie = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth'
url_MostPopular = 'https://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm'
url_Mtest = 'https://www.imdb.com/search/title/?genres=thriller&title_type=feature&sort=moviemeter'

def format(url = url_Movie, num_Movies = 5, headline_category = 'business', num_Headlines = 5):
    output = return_numHeadlinesMod('business', num_Headlines)
    return output

# The notifier function
def notify(title, message):
    t = '-title {!r}'.format(title)
    # s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    # s2 = '-subtitle {!r}'.format(subtitle)
    # m2 = '-message {!r}'.format(message2)
    os.system('terminal-notifier {}'.format(' '.join([m, t])))

if __name__ == "__main__":
    newsList = format()
    movieList = get_topMod(url_Movie, 5)
    for i in range(len(newsList)):
        output = newsList[i] + 'Top Movie: ' + movieList[i]
        notify(title = 'NEWS UPDATE', message = str(output))
        time.sleep(45)