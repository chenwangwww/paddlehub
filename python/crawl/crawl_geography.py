import requests
from bs4 import BeautifulSoup
from dbGeoCtr import geoctr
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import random

geography_url = 'https://you.ctrip.com/searchsite/Sight?query='

def geo_insertData(tb, data):
    geo_list = data[::2]
    loc_list = data[1::2]
    for i in range(len(geo_list)):
        res = {}
        res['geo'] = geo_list[i].get_text()
        res['geo_link'] = geo_list[i].get('href')
        res['loc'] = loc_list[i].get_text()
        res['loc_link'] = loc_list[i].get('href')
        geoctr.insertData(tb, res)

def search_save_geo_all(location):
    i = 1
    tb_name = location + '_景区'
    while(True):
        url = geography_url + location + '&PageNo=' + str(i)
        print(url)
        strhtml = requests.get(url)
        soup = BeautifulSoup(strhtml.text, 'lxml')
        search_list = soup.select('body > div.content.cf > div.main > div.search-content.cf > div > div.result > ul > li > dl > dt > a')
        print(i, len(search_list))
        if len(search_list) == 0:
            break
        else:
            if i == 1:
                geoctr.createTb(tb_name)
            geo_insertData(tb_name, search_list)
        i+=1

# search_save_geo_all('葫芦岛')

# geoctr.getAllTbs()


def timing_get_save_geo():
    print(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
    results = geoctr.getAllTbs()
    results_no_geo = list(filter(lambda x: x[0].split('_')[-1] != '景区', results))
    results_geo = list(filter(lambda x: x[0].split('_')[-1] == '景区', results))
    results_get = list(filter(lambda x: (x[0].split('_')[-1] + '_景区',) not in results_geo, results_no_geo))

    length_get = len(results_get)
    choose_one = random.randint(0, length_get-1)
    search_save_geo_all(results_get[choose_one][0].split('_')[-1])
    print(results_get[choose_one][0].split('_')[-1])
    print(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))

sched = BlockingScheduler()
sched.add_job(timing_get_save_geo, 'date', run_date='2021-01-14 10:59:10')
sched.start()
