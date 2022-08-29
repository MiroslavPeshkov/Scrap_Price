import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import re
import lxml
import streamlit as st
import openpyxl
from openpyxl import Workbook
import numpy as np
import datetime
import random

c = {'ASP.NET_SessionId': 'uspd4czxuxtaiqokiilppwpf',
     '_gat': '1',
     '.AspNet.cpsAuth': 'CfDJ8GaK_vc8ictOkQAmLJSxb4QNGXklQcHQEGVvBsc_rKicZdF-XXkLQH4zUAzKjGKa83S9NZJTiWzKwtsN9G3LZ1W5Mfuqwa6fLisyXbWBK83518JQBYjOuiBMoNkGFUsxvBmJqWggeHyrCBXIU-BR6uxi5oMlZjQcaGFDPoQ1_-H7xZxdcbdmL92Ck62Wi7spacXKvviGoo_qkBzUqVXeMGoKQFKlLh3T-f66kKuZk5FeMOFCaIKdTnCIR4G-IywuxjUzGJPYl_OlnG8B-K00qd7K8nVbuwRnan2gHqnZyiB2xtAia6D4fE8-Ef8Auph5Ka1uFiOmjUbjtuCujUaQdXIxoKveaeeZuEYW49ky6ZpNVpSeoWgPlEXwH99YHf2yXHX9xqjtY1YGRlgyLgF0_hRcrjNSvD3uFb5VlwYS0qZT6anGvF4vN_PZuCZES32x50bm8ZfDebQFZyL3-euLBN3C7H0RzgyzeFqbEnTNCtd-JXpjKJgLbiZqOtQXYDsvJyckhESjlC8xXRwzaDnKWb_4fEJ68vp_v76kVSVLfLh0',
     'U2DA5BAE510384E938A713A1FB26F4236': 'CfDJ8GaK_vc8ictOkQAmLJSxb4QNGXklQcHQEGVvBsc_rKicZdF-XXkLQH4zUAzKjGKa83S9NZJTiWzKwtsN9G3LZ1W5Mfuqwa6fLisyXbWBK83518JQBYjOuiBMoNkGFUsxvBmJqWggeHyrCBXIU-BR6uxi5oMlZjQcaGFDPoQ1_-H7xZxdcbdmL92Ck62Wi7spacXKvviGoo_qkBzUqVXeMGoKQFKlLh3T-f66kKuZk5FeMOFCaIKdTnCIR4G-IywuxjUzGJPYl_OlnG8B-K00qd7K8nVbuwRnan2gHqnZyiB2xtAia6D4fE8-Ef8Auph5Ka1uFiOmjUbjtuCujUaQdXIxoKveaeeZuEYW49ky6ZpNVpSeoWgPlEXwH99YHf2yXHX9xqjtY1YGRlgyLgF0_hRcrjNSvD3uFb5VlwYS0qZT6anGvF4vN_PZuCZES32x50bm8ZfDebQFZyL3-euLBN3C7H0RzgyzeFqbEnTNCtd-JXpjKJgLbiZqOtQXYDsvJyckhESjlC8xXRwzaDnKWb_4fEJ68vp_v76kVSVLfLh0',
     '_ga': 'GA1.2.892393629.1661620881',
     '_gid': 'GA1.2.1909818050.1661620881'}
st.title('Get matches results')
but = st.button('Launch')
if but:
    res = requests.get('https://old.baltbet.ru/BetsTota.aspx?page=1', cookies=c)
    soup = BeautifulSoup(res.text, 'lxml')
    pag = soup.find('div', {'class': 'pages'})
    pag = pag.find_all('a')[1].text
    pag = int(pag)
    data = []
    for num in range(1, 6):  # pag+1
        st.write('Work with page number - ', num)
        res = requests.get('https://old.baltbet.ru/BetsTota.aspx?page={num}', cookies=c)
        soup = BeautifulSoup(res.text, 'lxml')
        list_1 = soup.find('table', {'class': 'totalmain'}).find_all('a')
        list_2 = ['https://old.baltbet.ru/' + i.get('href') for i in list_1]
        count = 0
        for l in list_2[:5]:
            count += 1
            print('Page - ', num, 'Work - ', l, 'count - ', count)
            res = requests.get(l, cookies=c)
            time.sleep(random.uniform(0.3, 0.8))
            soup = BeautifulSoup(res.text, 'lxml')
            table = soup.find('table', {'class': 'betinfo2'})
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
    data_2 = []
    data = list(filter(None, data))
    data_1 = [j for i in data for j in i if len(j) == 1 or len(j) == 2]
    for i in data_1:
        data_2.append(i)
        data_2.append(' ')
    df = pd.DataFrame(data_2, columns=['Result'])
    df = df.T
    now_date = datetime.datetime.now().strftime('%Y-%m-%d')
    writer = pd.ExcelWriter(f'Result_list_{now_date}.xlsx')
    df.to_excel(writer, index=False)
    writer.save()
    st.write('Excel done')
    with open(f'Result_list_{now_date}.xlsx', "rb") as file:
        st.download_button(
            label="Download data as EXCEL",
            data=file,
            file_name=f'Result_list_{now_date}.xlsx',
            mime='text/xlsx',
        )


# import requests
# from bs4 import BeautifulSoup
# import time
# import csv
# import pandas as pd
# import re
# import datetime
# import streamlit as st
# import numpy as np
# from shutil import which
# import os
# import selenium
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import json
# import gspread
# from gspread_dataframe import get_as_dataframe, set_with_dataframe


# firefoxOptions = Options()
# FIREFOXPATH = which("firefox")
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
# firefoxOptions.add_argument(f'user-agent={user_agent}')
# firefoxOptions.add_argument('--headless')
# firefoxOptions.add_argument('--no-sandbox')
# firefoxOptions.add_argument("--window-size=1920,1080")
# firefoxOptions.add_argument('--disable-dev-shm-usage')
# firefoxOptions.add_argument('--ignore-certificate-errors')
# firefoxOptions.add_argument('--allow-running-insecure-content')
# firefoxOptions.binary = FIREFOXPATH

# all_links = ['https://e-neon.ru/svetodiodyi/',
#              'https://e-neon.ru/moschnyie-svetodiodyi/']

# all_links1 = [
#     'https://planar.spb.ru/led-other?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)',
#     'https://planar.spb.ru/goodssection/635?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)',
#     'https://planar.spb.ru/led-edison?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)',
#     'https://planar.spb.ru/goodssection/705?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)',
#     'https://planar.spb.ru/led-cree?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)',
#     'https://planar.spb.ru/led-osram?filter=~(diapasons~()~pvs~()~free_balance~true~by_rating~true)']

# all_links2 = [
#     'https://www.platan.ru/cgi-bin/qweryv.pl/0w200276.html',
#     'https://www.platan.ru/cgi-bin/qweryv.pl/0w200077.html',
#     'https://www.platan.ru/cgi-bin/qweryv.pl/0w52474.html']

# all_links3 = [
#     'https://www.symmetron.ru/catalog/aktivnye-komponenty/optoelektronika/svetodiody/svetodiody-belye/filter/clear/apply/']


# @st.experimental_singleton
# def installff():
#     os.system('sbase install geckodriver')
#     os.system(
#         'ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver.exe')


# _ = installff()


# def connect_to_google_sheet(name):
#     google_key = {
#         "type": "service_account",
#         "project_id": "parsing-360910",
#         "private_key_id": "b78d533fa22f4480cf8b374466e409997fa4cf3e",
#         "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDK8oEixR13RAOh\nGL+v0cKgfRLXM9rBKukCnWX8A7rbl5PZaVD5iDwa2UO2hfI+rEU3mgyBMKshUmPl\nohwljlEKD6+csgTnlZelOu5BDvdMrkb7q4Y/jzuwxQYnIL4cNgPOyELXWde7GYAU\nitDcDaOG/no0KbVyEl+TfhespX1jwzt48IXniPvkEkJ36B5U+lWZUZJG1i4VBmlY\nGeaqjtUp1xUHhhZIkMkYYZ3kh8mKQYRGNq8dcX5rKAeDKFKbAvrq9E7hYqjl9nZC\ngvpksExxLRTTJPkiVLjjRGFoYftzIpqbrfjh1Zb34bnSBxcNoNm5kOYBMtoyYFxs\nl9hqN+rjAgMBAAECgf9LLd+ogbHopx6xDqSeUkCcMw5HqhiJy4YwRx5VvQv7TKtN\ns+B15NcJxcd6Vc7nEz87hFVy22new3vov6StmjVrBLnefL5UYOtMH13Nu+g1qlmh\nNmkEzTUkxoJWUaAbKJHrMpmQLOKS7LSwPLwiHZX2QU6uWW+y/MYVsnVn/ztJON/H\nBPakSm81htxrazcQNxjd0d+TzXZeKt45qFOqnRg4r41kN+H5cnMBFCd8WnlqHl9u\nwseXsaSsVEK9moMQZIU30mo4qW9mm1vPxtkibvY2Cu5feiBP+YtY+yrZVBEOkjpW\nZvKwLT4iNNabTcbp6tH7Vx7bck2TASz3ogcOU7UCgYEA+PUpuUmIMyLYKH/CDt28\n6Ps2vIZJDEHOCQvq1PW8dXWX/gaRyZ+HeiIq+CLTO1Z0jU4f4UV/M9JfPQ2PYykj\nL01neNyEPco+1i+b0+fDHOJ4wLQ7WVH6cYcFWWcBmOUE50s/7ig8Dm7IG+bQoOBj\nCH6rvJ1ToCOsmE/HGaCx3bUCgYEA0LAnx67dCRe2/N6l6/iNhn3vciY015RU+86W\n2737D51xpBFSCnP00ZFbj/yfhHsV+YezQBEoGB2VOr+/2H8t2inmAnGKT/HDEpJP\n/5XPrn4LrW5YTgxeQ8pn7tGyfzWPqMNBoTOjnjGBLCVRUgvfmpz+FJxhRMyicdq+\nwznxxTcCgYACGM6JKP1ksN5xOOJBjcyRicwkOl1TJRq/KMKJmKhFtP/au+Nud1GE\nzdTe0ixFS60fo5DRLOytWxBCS2Lxyt7o/xXoBrN2ccWluDDvz/vsuluaA+qcDfy2\nCBUbc6qnxwYLjK61KtGWrYgx8/e94yXyZF697/VMXACQJ9vdc2UMIQKBgEopb9mc\noNxsWxE+JoTXTaQv+Pn97eV2x0S9RAtPVntUHmCJ7zfbwXMATyO6SQ4Rl9uXh/IK\nps77JF8+aXUMrUTMgvr3UonahtKAwIE5whZmoMu/XQ5Pguhgc9MBHofqhuUYjqg0\n6756JUeE84NOyOXvSLQWZtLGTixb6lMCspK9AoGAIMeA+Pt4tS88leLn+IK6ru0r\n0twTwBw4nQwZRZ7pJS88apU84lHsb9VZUoXLcmeVgMqNR/hmqkQ176JsE+bNeHW7\nlrHTstXwM8xp18//b9NOBLCj4ocwrRCxnE9HX+Zfq+wfiRUNRbW7usC6PMqceOxQ\nA1DTLKLLY1vqpGcOEQc=\n-----END PRIVATE KEY-----\n",
#         "client_email": "parsing@parsing-360910.iam.gserviceaccount.com",
#         "client_id": "104700695693505507681",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/parsing%40parsing-360910.iam.gserviceaccount.com"}

#     with open("google_key_1.json", "w") as outfile:
#         json.dump(google_key, outfile)
#     creds = gspread.service_account(filename="google_key_1.json")
#     sh = creds.open("Парсинг")
#     worksheet = sh.worksheet(name)
#     return worksheet
# st.title('Парсинг')
# but = st.button('Пуск')
# def first():
#   CONCURENT = 'Neon'
#   ALL_URLS = []
#   for link in all_links:
#       res = requests.get(link)
#       time.sleep(0.5)
#       soup = BeautifulSoup(res.text, 'lxml')
#       pignatation = soup.find('ul', {'class': 'pagination'}).find_all('li')[-1].find('a').get('href').split('=')[
#           -1]
#       pignatation = int(pignatation)
#       all_urls = soup.find_all('a', {'itemprop': 'url'})
#       all_urls_ = [i.get('href') for i in all_urls]
#       ALL_URLS.extend(all_urls_)
#       print('PAG - ', pignatation)
#       for num in range(2, pignatation + 1):  # pignatation + 1
#           time.sleep(1.5)
#           ur = f'{all_links[0]}?page={num}'
#           res = requests.get(ur)
#           print('Work - ', ur)
#           soup = BeautifulSoup(res.text, 'lxml')
#           all_urls = soup.find_all('a', {'itemprop': 'url'})
#           all_urls_ = [i.get('href') for i in all_urls]
#           ALL_URLS.extend(all_urls_)

#   for l in ALL_URLS:
#       time.sleep(0.5)
#       print('W - ', l)
#       now_date = datetime.datetime.now().strftime("%Y-%m-%d")
#       res = requests.get(l)
#       soup = BeautifulSoup(res.text, 'lxml')

#       price = soup.find('span', {'class': 'product-price-product'}).text.replace('р.', '')

#       articl = soup.find('h1', {'itemprop': 'name'}).text.strip()

#       nalich = soup.find(text=re.compile('Наличие: ')).find_next('span').text
#       nalich_f = re.findall('[0-9]+', nalich.replace('\xa0', ''))
#       nalich_f = ''.join(nalich_f)

#       try:
#           pat_type = re.compile('\d+')
#           type_raz = soup.find(text=re.compile('Корпус')).find_next('td').text
#           type_raz = re.search(pat_type, type_raz)[0]
#       except:
#           type_raz = None

#       try:
#           CCT = soup.find(text=re.compile('Цветовая температура')).find_next('td').text
#       except:
#           CCT = None

#       try:
#           CRI = soup.find(text=re.compile('Индекс цветопередачи')).find_next('td').text
#       except:
#           CRI = None

#       try:
#           brand = soup.find(text=re.compile('Производитель')).find_next('td').text
#       except:
#           brand = None

#       series = None
#       try:
#           ibin = soup.find(text=re.compile('Ток')).find_next('td').text
#       except:
#           ibin = None

#       try:
#           Iмакс = soup.find(text=re.compile('Максимальный ток')).find_next('td').text
#       except:
#           Iмакс = None

#       try:
#           Фмин = soup.find(text=re.compile('Световой поток')).find_next('td').text
#       except:
#           Фмин = None

#       Фтип = None
#       Фмакс = None

#       # STATISCTICS FOR AVARAGE
#       try:
#           Uтип = soup.find(text=re.compile('Напряжение тип.')).find_next('td').text
#           Uмин = Uтип.split('-')[0].replace(',', '.')
#           Uмакс = Uтип.split('-')[-1].replace(',', '.')
#           Uмин = float(Uмин)
#           Uмакс = float(Uмакс)
#           Uном_В = round((Uмин + Uмакс) / 2)
#       except:
#           Uтип = None
#           Uмин = None
#           Uмакс = None
#           Uном_В = None
#       try:
#           Datasheet = soup.find_all('td', {'itemprop': 'value'})[-1].find('a').get('href')
#           Datasheet = 'https://e-neon.ru' + Datasheet
#       except:
#           Datasheet = None

#       with open(f'PARSING.csv', 'a', newline='', encoding='utf-8') as csvfile:
#           datawriter = csv.writer(csvfile, delimiter=',',
#                                   quotechar='"', quoting=csv.QUOTE_MINIMAL)
#           datawriter.writerow(
#               [now_date] + [CONCURENT] + [l] + [articl] + [type_raz] + [CCT] + [CRI] + [Uном_В] + [brand] + [
#                   price] + [nalich_f] + [series] + [ibin] + [Iмакс] + [Фмин] + [Фтип] + [Фмакс] + [Uмин] + [
#                   Uтип] + [
#                   Uмакс] + [Datasheet])


# def second():
#     CONCURENT = 'Планар'
#     ALL_URLS = []
#     ALL_PRICE = []
#     browser = webdriver.Firefox(executable_path=r'/home/appuser/venv/bin/geckodriver.exe', options=firefoxOptions)
#     for link in all_links1:
#         browser.implicitly_wait(7)
#         browser.get(link)
#         time.sleep(4)
#         but = browser.find_element(By.XPATH, "//select[@class = 'group-sm ng-pristine ng-valid']").click()
#         #     browser.execute_script("arguments[0].click();", but)
#         time.sleep(2)
#         but_click = browser.find_element(By.XPATH, "//option[@value = '150']").click()
#         time.sleep(2)
#         print(link)
#         html = browser.page_source
#         soup = BeautifulSoup(html, 'lxml')
#         all_urls = soup.find_all('a', {'class': 'ng-binding'})
#         all_urls_ = [i.get('href') for i in all_urls]
#         all_urls_ = ['https://planar.spb.ru' + i for i in all_urls_ if i != '#']
#         prices = soup.find_all('span', {'class': 'ng-scope ng-binding'})
#         prices_all = [i.text for i in prices]
#         ALL_PRICE.extend(prices_all)
#         print('Общее колво URL 2 сайт - ', all_urls_)
#         ALL_URLS.extend(all_urls_)

#     dict_ur_price = dict(zip(ALL_URLS, ALL_PRICE))
#     browser.quit()

#     for k, v in dict_ur_price.items():
#         res = requests.get(k)
#         time.sleep(0.7)
#         print('work - ', k)
#         now_date = datetime.datetime.now().strftime("%Y-%m-%d")
#         soup = BeautifulSoup(res.text, 'lxml')
#         articl = soup.find('h1', {'class': 'product-card__title'}).text.split(',')[0]
#         nalich_f = soup.find(text=re.compile('В наличии на складе')).find_next('span').text.replace('шт', '')
#         price = v
#         try:
#             type_raz = soup.find(text=re.compile('Типоразмер  LED')).find_next('span').text
#         except:
#             type_raz = None

#         try:
#             CRI = soup.find(text=re.compile('CRI Ra, не менее')).find_next('span').text
#         except:
#             CRI = None

#         try:
#             pat_CCT = re.compile(r'\d+')
#             CCT = soup.find(text=re.compile('CCT тип, K')).find_next('span').text.replace('+', '')
#             CCT = re.search(pat_CCT, CCT)[0]
#         except Exception as ex:
#             print(ex)
#             CCT = None

#         try:
#             brand = soup.find(text=re.compile('Производитель')).find_next('span').text
#         except:
#             brand = None

#         try:
#             series = soup.find(text=re.compile('Семейство')).find_next('span').text
#         except:
#             series = None

#         ibin = None

#         try:
#             Iмакс = soup.find(text=re.compile('Ток пр. макс, мА')).find_next('span').text
#         except:
#             Iмакс = None

#         Фмин = None
#         Фтип = None
#         try:
#             Фмакс = soup.find(text=re.compile('Свет. поток макс, лм')).find_next('span').text
#         except:
#             Фмакс = None

#         # STATISCTICS FOR AVARAGE
#         try:
#             Uтип = soup.find(text=re.compile('Напряжение тип, В')).find_next('span').text
#             Uтип = float(Uтип)
#             Uном_В = round((Uтип))
#         except:
#             Uтип = None
#             Uном_В = None
#         Uмин = None
#         Uмакс = None

#         try:
#             Datasheet = soup.find('a', {'class': 'product-card-content__wrapper'}).get('href')
#         except:
#             Datasheet = None

#         with open(f'PARSING.csv', 'a', newline='', encoding='utf-8') as csvfile:
#             datawriter = csv.writer(csvfile, delimiter=',',
#                                     quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             datawriter.writerow(
#                 [now_date] + [CONCURENT] + [k] + [articl] + [type_raz] + [CCT] + [CRI] + [Uном_В] + [brand] + [
#                     price] + [nalich_f] + [series] + [ibin] + [Iмакс] + [Фмин] + [Фтип] + [Фмакс] + [Uмин] + [
#                     Uтип] + [
#                     Uмакс] + [Datasheet])


# def third():
#     CONCURENT = 'Платан'
#     ALL_URLS = []
#     for lin in all_links2:
#         print(lin)
#         res = requests.get(lin)
#         time.sleep(0.7)
#         soup = BeautifulSoup(res.text, 'lxml')
#         all_links = soup.find_all('a', {'class': 'link'})
#         all_links_ = [i.get('href') for i in all_links]
#         all_links_ = ['https://www.platan.ru' + i for i in all_links_ if i != None and 'id' in i]
#         ALL_URLS.extend(all_links_)
#         pag = soup.find_all('span', {'id': 'pagination1'})[-1].find('b').text
#         pag = int(pag)
#         for num in range(2, pag + 1):
#             li = lin.replace('0w', f'{num}w')
#             print(li)
#             res = requests.get(li)
#             soup = BeautifulSoup(res.text, 'lxml')
#             all_links = soup.find_all('a', {'class': 'link'})
#             all_links_ = [i.get('href') for i in all_links]
#             all_links_ = ['https://www.platan.ru' + i for i in all_links_ if i != None and 'id' in i]
#             ALL_URLS.extend(all_links_)

#     for l in ALL_URLS:
#         time.sleep(0.7)
#         print('Work - ', l)
#         now_date = datetime.datetime.now().strftime("%Y-%m-%d")
#         res = requests.get(l)
#         pattern = re.compile(r'\d+')
#         pattern1 = re.compile(r'\d+ шт')
#         soup = BeautifulSoup(res.text, 'lxml')

#         all_fetch = soup.find('h1', {'itemprop': 'name'}).text

#         try:
#             articl = all_fetch.split(',')[0]
#         except:
#             articl = None

#         patern_svet = re.compile(r'светодиод \d+')
#         try:
#             type_raz = re.search(patern_svet, all_fetch)[0]
#         except:
#             type_raz = None

#         pattern_cct = re.compile(r'\d+K')
#         try:
#             CCT = re.search(pattern_cct, all_fetch)[0].replace('K', '')
#         except:
#             CCT = None

#         pattern_cri = re.compile(r'CRI\d+')
#         try:
#             CRI = re.search(pattern_cri, all_fetch)[0]
#         except:
#             CRI = None

#         try:
#             brand = soup.find(text=re.compile('Производитель')).find_next('a').text
#         except:
#             brand = None

#         pattern_u = re.compile(r',.\S+В')
#         try:
#             Uтип = re.search(pattern_u, all_fetch)[0]
#             Uтип = Uтип.split(',')[-1]
#             Uтип = Uтип.replace('В', '').strip()
#             Uтип = float(Uтип)
#             Uном_В = round((Uтип))
#         except:
#             Uтип = None
#             Uном_В = None

#         try:
#             price = soup.find_all('td', {'class': 'left-align'})
#             price = [i.text for i in price]
#             price = price[-1].split('-')[-1]
#             price = re.search(pattern, price)[0]
#             price = float(price)
#         except:
#             price = None

#         try:
#             nalich_f = soup.find('tr', {'style': 'background-color: #;'}).text.replace('\xa0', '').replace('\n',
#                                                                                                            ' ')
#             nalich_f = re.search(pattern1, nalich_f)[0]
#             nalich_f = nalich_f.split(' ')[0]
#         except:
#             nalich_f = None

#         series = None
#         ibin = None
#         Iмакс = None
#         Фмин = None
#         Фтип = None
#         Фмакс = None
#         Uмин = None
#         Uмакс = None
#         Datasheet = None

#         with open(f'PARSING.csv', 'a', newline='', encoding='utf-8') as csvfile:
#             datawriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             datawriter.writerow(
#                 [now_date] + [CONCURENT] + [l] + [articl] + [type_raz] + [CCT] + [CRI] + [Uном_В] + [brand] + [
#                     price] + [nalich_f] + [series] + [ibin] + [Iмакс] + [Фмин] + [Фтип] + [Фмакс] + [Uмин] + [
#                     Uтип] + [
#                     Uмакс] + [Datasheet])


# def forth():
#     CONCURENT = 'Symmetron'
#     ALL_LINKS = []
#     for i in all_links3:
#         print(i)
#         res = requests.get(i)
#         soup = BeautifulSoup(res.text, 'lxml')
#         links_all = soup.find_all('a', {'class': 'item-info__fullLink'})
#         links_all_ = ['https://www.symmetron.ru' + i.get('href') for i in links_all]
#         ALL_LINKS.extend(links_all_)
#         for num in range(2, 19):
#             time.sleep(1)
#             ur = f'{i}?PAGEN_1={num}'
#             res = requests.get(ur)
#             print(ur)
#             soup = BeautifulSoup(res.text, 'lxml')
#             links_all = soup.find_all('a', {'class': 'item-info__fullLink'})
#             links_all_ = ['https://www.symmetron.ru' + i.get('href') for i in links_all]
#             ALL_LINKS.extend(links_all_)

#     for l in ALL_LINKS:
#         print(l)
#         now_date = datetime.datetime.now().strftime("%Y-%m-%d")
#         response = requests.get(l)
#         soup = BeautifulSoup(response.text, 'lxml')

#         try:
#             articl = soup.find('h1').text.replace('\n', '').strip().split(' ')[0]
#         except:
#             articl = None

#         try:
#             type_raz = soup.find(text=re.compile('Типоразмер')).find_next('span').find_next('span').text
#         except:
#             type_raz = None

#         try:
#             CCT = soup.find(text=re.compile("CCT тип.")).find_next('span').find_next('span').text
#             pat_cct = re.compile(r'\d+')
#             CCT = re.search(pat_cct, CCT)[0]
#         except:
#             CCT = None

#         try:
#             CRI = soup.find(text=re.compile("CRI,Ra")).find_next('span').find_next('span').text
#         except:
#             CRI = None

#         try:
#             brand = soup.find(text=re.compile(" Производитель ")).find_next('span').find_next('span').text
#         except:
#             brand = None

#         try:
#             price = soup.find('span', {'class': 'quantity-price'}).text.split(' ')[0]
#         except:
#             price = None

#         try:
#             nalich_f = soup.find('div', {'class': 'totalIn'}).text.replace('\n', '').strip()
#             pat_nal = re.compile(r'\d+')
#             nalich_f = re.search(pat_nal, nalich_f)[0]
#         except:
#             nalich_f = None
#         try:
#             series = soup.find(text=re.compile("Серия")).find_next('span').find_next('span').text
#         except:
#             series = None

#         text = soup.find('section', {'class': 'detail'}).text.replace('\n', ' ').replace('\r', ' ').strip()
#         try:
#             if_bin_pat = re.compile(r'If\(bin\): \d+ мА')
#             ibin = re.search(if_bin_pat, text)[0].split(':')[-1].strip().split(' ')[0]
#         except:
#             ibin = None
#         try:
#             imax_pat = re.compile(r'If\(max\): \d+ мА')
#             Iмакс = re.search(imax_pat, text)[0].split(':')[-1].strip().split(' ')[0]
#         except:
#             Iмакс = None

#         try:
#             Фмин_pat = re.compile(r'Φv.\(bin\)min: \d+ лм')
#             Фмин = re.search(Фмин_pat, text)[0].split(':')[-1].strip().split(' ')[0]
#         except:
#             Фмин = None

#         try:
#             Фмакс_pat = re.compile(r'Φv.\(bin\)max: \d+ лм')
#             Фмакс = re.search(Фмакс_pat, text)[0].split(':')[-1].strip().split(' ')[0]
#         except:
#             Фмакс = None

#         Фтип = None

#         try:
#             Uмин_pat = re.compile(r'Uf\(min\):.+В;')
#             Uмин = re.search(Uмин_pat, text)[0].replace('В', '').replace(';', '').split(':')[-1].strip().split(' ')[
#                 0]
#             Uмин = float(Uмин.replace(',', '.'))
#         except:
#             Uмин = None

#         try:
#             Uмакс_pat = re.compile(r'Uf\(max\):.+В[.;]')
#             Uмакс = \
#             re.search(Uмакс_pat, text)[0].replace('В', '').replace(';', '').split(':')[-1].strip().split(' ')[0]
#             Uмакс = float(Uмакс.replace(',', '.'))
#         except:
#             Uмакс = None

#         if Uмакс and Uмин:
#             Uном_В = round((Uмин + Uмакс) / 2)
#         else:
#             if Uмакс:
#                 Uном_В = round(Uмакс)
#             elif Uмин:
#                 Uном_В = round(Uмин)
#             else:
#                 Uном_В = None

#         try:
#             Datasheet = soup.find_all('a', {'target': '__blank'})
#             Datasheet = [i.get('href') for i in Datasheet]
#             Datasheet = set(Datasheet)
#             Datasheet = list(Datasheet)
#             Datasheet = ', '.join(Datasheet)
#         except:
#             Datasheet = None

#         Uтип = None

#         with open(f'PARSING.csv', 'a', newline='', encoding='utf-8') as csvfile:
#             datawriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             datawriter.writerow(
#                 [now_date] + [CONCURENT] + [l] + [articl] + [type_raz] + [CCT] + [CRI] + [Uном_В] + [brand] + [
#                     price] + [nalich_f] + [series] + [ibin] + [Iмакс] + [Фмин] + [Фтип] + [Фмакс] + [Uмин] + [
#                     Uтип] + [
#                     Uмакс] + [Datasheet])


# def clean_data():
#     df_all = pd.read_csv('PARSING.csv')
#     df_all = df_all.drop_duplicates(subset=['Дата', 'Артикул'])
#     df_all = df_all.dropna(subset=['Uнoм,В', 'CRI', 'Цена', 'Остаток', 'CCT'])
#     df_all['Цена'] = df_all['Цена'].fillna('0')
#     df_all['Остаток'] = df_all['Остаток'].fillna('0')
#     df_all = df_all.reset_index()
#     del df_all['index']
#     pattern = re.compile(r'\d+')
#     df_all['Остаток'] = df_all['Остаток'].apply(lambda x: re.search(pattern, str(x))[0])
#     df_all['Цена'] = df_all['Цена'].replace(r'[а-яА-Я]', np.nan, regex=True)
#     df_all['Цена'] = df_all['Цена'].apply(lambda x: str(x).replace(',', '.').strip())
#     df_all['Цена'] = df_all['Цена'].apply(lambda x: str(x).strip())
#     df_all['Остаток'] = df_all['Остаток'].fillna('0')
#     df_all['Цена'] = df_all['Цена'].apply(lambda x: float(x))
#     df_all['Остаток'] = df_all['Остаток'].apply(lambda x: float(x))
#     trual = df_all.sort_values(by=['Артикул', 'Дата'])
#     trual['Дельта цена'] = trual[['Артикул', 'Цена']].groupby('Артикул').diff()
#     trual['Дельта Остаток'] = trual[['Артикул', 'Остаток']].groupby('Артикул').diff()
#     trual['Цена'] = trual['Цена'].fillna(float(0))
#     trual['Дельта цена'] = trual['Дельта цена'].fillna('-')
#     trual['Дельта Остаток'] = trual['Дельта Остаток'].fillna('-')
#     trual = trual.fillna('')
#     trual = trual.reset_index()
#     del trual['index']
#     trual['Дельта цена'] = trual['Дельта цена'].apply(lambda x: str(x).replace('-', ''))
#     trual['Дельта Остаток'] = trual['Дельта Остаток'].apply(lambda x: str(x).replace('-', ''))
#     # trual_2 = trual.sort_values(by=['Дата', 'Дельта цена'], ascending=False, na_position='last')
#     # trual_2 = trual_2.reset_index()
#     # del trual_2['index']
#     # trual_2['Дельта цена'] = trual_2['Дельта цена'].apply(lambda x: round(float(x), 2) if x != '' else '')
#     # trual_2['Дельта Остаток'] = trual_2['Дельта Остаток'].apply(lambda x: round(float(x), 2) if x != '' else '')
#     return trual


# def post_to_gs(name_1, df_1):
#     worksheet_1 = connect_to_google_sheet(name_1)
#     worksheet_1.clear()
#     set_with_dataframe(worksheet_1, df_1)
#     print('Post df_1 to gs')

# if __name__ == '__main__':
#     if but:
#         first()
#         second()
#         third()
#         forth()
#         trual = clean_data()
#         name_1 = 'База данных'
#         post_to_gs(name_1, trual)
#         st.write('Post to GS')
