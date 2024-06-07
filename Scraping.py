from bs4 import BeautifulSoup
import requests
import openpyxl

try:
    response = requests.get('https://www.gadgets360.com/entertainment/new-hindi-movies')
    soup=BeautifulSoup(response.text,'html.parser')
    # print(soup)

    movies_list = soup.find("div",id='all_movies').find_all("div",class_="_mvbx")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['No.', 'Movie Name', 'Cast', 'Release Date', 'Category', 'Director'])
    
    counter = 1

    for movies in movies_list:
        movie_name= movies.find('h3').a.text
        movie_cast= movies.find('li',class_='lclamp').text
        release_date= movies.find('div',class_="_flx").text
        category= movies.find('li',class_="_mvgenre").get_text(strip=True)
        director= movies.find('li',class_="_mvdrc").text.split('Director')[1]

        ws.append([counter, movie_name, movie_cast, release_date, category, director])
        #print(counter, movie_name, movie_cast, release_date, category, director)
        counter += 1

    wb.save('movies.xlsx')
except Exception as e:
    print(e)




