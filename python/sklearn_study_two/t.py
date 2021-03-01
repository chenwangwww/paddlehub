import requests
from bs4 import BeautifulSoup

root_url = 'https://you.ctrip.com'
geography_url = 'https://you.ctrip.com/searchsite/Sight?query='
info_arr = []

def crawl_geo(suburl):
    url = root_url + suburl
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    content = soup.select('#__next > div.poiDetailPageWrap > div > div.baseInfoModule > div.baseInfoMain > div.title > h1')[0].get_text()
    title_list = soup.select('#__next > div.poiDetailPageWrap > div > div.baseInfoModule > div.baseInfoMain > div.baseInfoContent > div.baseInfoItem')
    for item in title_list:
        subps = item.find_all('p')
        if len(subps) ==2 :
            info = {'content': content, 'target': subps[1].get_text(), 'pred': subps[0].get_text(), 'envir': '小明教小陈'}
            info_arr.append(info)
    

# crawl_geo()

def crawl_geo_search(name):
    info_arr = []
    url = geography_url + name
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    search_list = soup.select('body > div.content.cf > div.main > div.search-content.cf > div > div.result > ul > li > dl > dt > a')
    if len(search_list) == 0:
        pass
    else:
        geo_link = search_list[0].get('href')
        crawl_geo(geo_link)

# crawl_geo_search('故宫')