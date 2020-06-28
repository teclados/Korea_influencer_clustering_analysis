from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium import webdriver

# 첫번째 데이터 수집 단계
# beauty influencer 1000명의 account를 featuring 사이트에서 수집

# -------------------------------selenium----------------------------------

driver = webdriver.Chrome('C:/Users/aaa/Downloads/chromedriver_win32/chromedriver.exe')  # web 드라이브 위치
# featuring 로그인
url = "https://featuring.co/accounts/login/"
driver.get(url)
time.sleep(4)
driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/div[2]/form/p[1]/input').send_keys("아이디")
driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/div[2]/form/p[2]/input').send_keys("비밀번호")
driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/div[2]/form/button').click()
time.sleep(3)
driver.get('https://featuring.co/report/')
time.sleep(2)  # 데이터 껍데기 기다리기
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/div[1]/img[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[15]/div').click()
time.sleep(2)

# ----------------------------beautifulsoup-------------------------------

pageString = driver.page_source
bsObj = bs(pageString, "html.parser")
bs_list = bsObj.select(".bookmark-list")
account_list = list()
for book in bs_list:
    account = book.find('a')['href']
    account_list.append(account)

for i in range(2, 11):
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[2]/div[{}]'.format(i)).click()
    time.sleep(5)
    pageString = driver.page_source
    bsObj = bs(pageString, "html.parser")
    bs_list = bsObj.select(".bookmark-list")
    for book in bs_list:
        account = book.find('a')['href']
        account_list.append(account)

driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[2]/img[2]').click()
time.sleep(10)

pageString = driver.page_source
bsObj = bs(pageString, "html.parser")
bs_list = bsObj.select(".bookmark-list")
for book in bs_list:
    account = book.find('a')['href']
    account_list.append(account)

for j in range(1, 10):
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[3]/div[2]/div[{}]'.format(j + 1)).click()
    time.sleep(5)
    pageString = driver.page_source
    bsObj = bs(pageString, "html.parser")
    bs_list = bsObj.select(".bookmark-list")
    for book in bs_list:
        account = book.find('a')['href']
        account_list.append(account)

print(len(account_list))
print(account_list[0])

result = list()
for n in range(len(account_list)):
    popular_account = account_list[n]
    temp = [popular_account]
    result.append(temp)

data = pd.DataFrame(result)
data.to_csv('beauty_influencer_account.csv', encoding='utf-8-sig')
