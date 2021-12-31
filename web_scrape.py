from bs4 import BeautifulSoup
import requests
import re

# Downloading imdb top 250 movie's data
url = 'https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=1RRPC78W0W96HAYWKY07&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('div.lister-item-content')
list = []

for i in range(len(movies)):
    title_raw = [b.text for b in movies[i].select('a')]
    title = title_raw[0]
    # ratings = [b.attrs.get('data-value') for b in soup.select('div.ratings-bar strong')]
    year = [b.text for b in movies[i].select('h3.lister-item-header span[class="lister-item-year text-muted unbold"]')]
    runtime = [b.text for b in movies[i].select('p.text-muted span[class=runtime]')]
    mprating = [b.text for b in movies[i].select('p.text-muted span[class=certificate]')]
    description_raw = [b.text for b in movies[i].select('div.lister-item-content p[class="text-muted"]')]
    description = description_raw[1::2]
    rating = [b.attrs.get('data-value') for b in movies[i].select('div[class="inline-block ratings-imdb-rating"]')]
    # votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
    # print(title, "\n", year, "\n", runtime, "\n", mprating, "\n")

    data = {"title": title,
            "year": year,
            "runtime": runtime,
            "mprating": mprating,
            "description": description,
            "rating": rating}

    list.append(data)

print(list[0])
# create a empty list for storing
# movie information
# list = []
 
# Iterating over movies to extract
# each movie's details
# for index in range(0, len(movies)):
   
#     data = {"movie_title": movie_title,
#             "year": year,
#             "rank": rank,
#             "rating": ratings[index],
#             "vote": votes[index],
#             "link": links[index]}
#     list.append(data)

#     # printing movie details with its rating.
# for movie in list:
#     print(movie['rank'], '-', movie['movie_title'], '('+movie['year'] +
#           ') -', movie['rating'])