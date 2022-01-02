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
    title = str(title_raw[0])
    year = str([b.text for b in movies[i].select('h3.lister-item-header span[class="lister-item-year text-muted unbold"]')])
    year = re.sub("\D", "", year)[0:4]
    runtime = str([b.text for b in movies[i].select('p.text-muted span[class=runtime]')])
    runtime = re.sub("\D", "", runtime)
    mprating = str([b.text for b in movies[i].select('p.text-muted span[class=certificate]')])
    mprating = mprating.strip("[]'")
    description = [b.text for b in movies[i].select('div.lister-item-content p[class="text-muted"]')]
    description = str(description[1::2])
    description = description.strip("[]'\"").lstrip("\\n")
    rating = str([b.attrs.get('data-value') for b in movies[i].select('div[class="inline-block ratings-imdb-rating"]')])
    rating = rating.strip("[]'")
    rank = str(i + 1)

    data = {"rank": rank,
            "title": title,
            "year": year,
            "runtime": runtime,
            "mprating": mprating,
            "description": description,
            "rating": rating}

    list.append(data)

for movie in list:
    print("Rank: " + movie['rank'] + "\nTitle: " + movie['title'] + "\nRelease Year: " + movie['year'] + "\nRuntime: " + 
    movie['runtime'] + " minutes" + "\nMotion Picture Rating: " + movie['mprating'] + "\nDescription: " + movie['description'] + 
    "\nRating: " + movie['rating'] + "\n")