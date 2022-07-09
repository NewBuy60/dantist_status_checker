import requests
import send_email
from bs4 import BeautifulSoup
import lxml

url = 'https://reg03.k-vrachu.ru/service/schedule/8288/0/doctors?per_page=40&page=2'
r = requests.get(url)

with open('page.txt', 'w') as page:
    page.write(r.text)

with open('page.txt') as fp:
    soup = BeautifulSoup(fp, 'lxml')

list_of_dantists = soup.find(id='lpuunit_1129').find_all(class_='doc-row')

list_urls = []
for dantist in list_of_dantists:

    url = dantist.find('a').get('href')
    list_urls.append(url)

flag = 0
for url in list_urls[0:1]:

    page = requests.get(f'https://reg03.k-vrachu.ru{url}')   
    soup = BeautifulSoup(page.text, 'lxml')
    dantist_name = soup.find('span', class_='docname').text
    items = soup.find(['table', 'timeTable slick-slide slick-active']).find_all('td')
    for item in items:
        
        if item.get('class') == ['free']:
            
            print(f"{dantist_name} имеет свободное время для записи!")
            send_email.send_email(f"{dantist_name} имеет свободное время для записи!\n'https://reg03.k-vrachu.ru{url}")
            flag = 1
            break
    
    if flag == 1:
        break

if flag == 0:
    print("Нет свободного времени для записи!")