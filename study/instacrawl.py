from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import time
from selenium.webdriver.common.by import By


def insta_searching(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url


def select_first(driver):
    first = driver.find_elements(By.CSS_SELECTOR, "div._aagw")[0]
    first.click()
    time.sleep(3)


import re
from bs4 import BeautifulSoup


def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    try:
        content = soup.select('div._a9zs')[0].text
    except:
        content = ''
    tags = re.findall(r'#[^\s#,\\]+', content)
    date = soup.select('time._aaqe')[0]['datetime'][:10]

    try:
        like = soup.select('div._aacl._aaco._aacw._aacx._aada._aade')[0].findAll('span')[-1].text
    except:
        like = 0

    try:
        place = soup.select('div._aaqm')[0].text
    except:
        place = ''

    data = [content, date, like, place, tags]
    return data


def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh")
    right.click()
    time.sleep(3)


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.instagram.com')
time.sleep(3)

email =
input_id = driver.find_elements(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')[0]

input_id.clear()
input_id.send_keys(email)

password =
input_pw = driver.find_elements(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')[0]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(5)

word = input('검색어를 입력하세요 : ')
word = str(word)
url = insta_searching(word)

driver.get(url)
time.sleep(10)

select_first(driver)

results = []
target = 10000
for i in range(target):
    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except:
        time.sleep(2)
        move_next(driver)
    time.sleep(5)

print(results[:2])

import pandas as pd
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

results_df = pd.DataFrame(results)
results_df.columns = ['content', 'date', 'like', 'place', 'tags']
results_df.to_excel(date + '_about ' + word + ' insta crawling.xlsx')