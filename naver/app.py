import requests
from bs4 import BeautifulSoup

현대에너지솔루션데이터 = requests.get('https://finance.naver.com/item/sise.naver?code=322000')

현대에너지솔루션soup = BeautifulSoup(현대에너지솔루션데이터.content, 'html.parser')
no_up = 현대에너지솔루션soup.find_all('span', class_='blind')[12]
rate = 현대에너지솔루션soup.select('.no_down span')
print(no_up.text,rate[14].text,rate[15].text,rate[20].text)

OCI데이터 = requests.get('https://finance.naver.com/item/main.naver?code=010060')

OCIsoup = BeautifulSoup(OCI데이터.content, 'html.parser')
no_up = OCIsoup.find_all('span', class_='blind')[12]
rate = OCIsoup.select('.no_down span')
print(no_up.text,rate[13].text,rate[14].text,rate[19].text)


