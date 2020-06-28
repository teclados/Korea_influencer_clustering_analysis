from bs4 import BeautifulSoup as bs
import time
import pandas as pd

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import timeit

driver = webdriver.Chrome('C:/Users/aaa/Downloads/chromedriver_win32/chromedriver.exe')

# -------------------------------------------------------------------------
# 인스타 로그인
# url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
# driver.get(url)
# time.sleep(4)
#
# driver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
#     "로그인")
# driver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(
#     "로그인")
# driver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
# time.sleep(3)
# ------------------------------------------------------------------------

start = timeit.default_timer()

beauty_data = pd.read_csv('./beauty_basic_info.csv')
box_list = list()
print(beauty_data['account'][939])
for i in range(900, 939):
    account_link = beauty_data['account'][i]
    driver.get(account_link)
    time.sleep(1.8)
    pageString = driver.page_source
    bsObj = bs(pageString, 'html.parser')
    bs_list = bsObj.select('.v1Nh3')

    image_love = []
    image_comment = []
    video_love = []
    video_comment = []
    igtv_love = []
    igtv_comment = []

    for j in bs_list:
        image_video_igtv = 'video'
        video_list = j.select(".u7YqG > span[aria-label = 동영상]")
        IGTV_list = j.select(".u7YqG > span[aria-label = IGTV]")
        if len(video_list) == 0:
            if len(IGTV_list) == 0:
                image_video_igtv = 'image'
            else:
                image_video_igtv = 'igtv'

        p_link = j.find('a')['href']
        hove = driver.find_element_by_xpath(
            "//div[@class='Nnq7C weEfm']/div[@class='v1Nh3 kIKUG  _bz0w']/a[@href='{}']".format(p_link))
        action = ActionChains(driver)
        action.move_to_element(hove).perform()
        time.sleep(0.3)
        pageString2 = driver.page_source
        bsObj2 = bs(pageString2, "html.parser")
        bs_list2 = bsObj2.select("div.qn-0x > ul > li > span")

        if len(bs_list2) != 4:
            continue

        # 좋아요 수 예외처리
        love = bs_list2[0].text
        if love.find("백만") >= 0:
            if love.find(".") >= 0:
                love = int("".join(filter(str.isdigit, love))) * 100000
            else:
                love = int("".join(filter(str.isdigit, love))) * 1000000
        elif love.find("천") >= 0:
            if love.find(".") >= 0:
                love = int("".join(filter(str.isdigit, love))) * 100
            else:
                love = int("".join(filter(str.isdigit, love))) * 1000
        else:
            love = int("".join(filter(str.isdigit, love)))
        # 댓글 수 예외처리
        comment = bs_list2[2].text
        if comment.find("백만") >= 0:
            if comment.find(".") >= 0:
                comment = int("".join(filter(str.isdigit, comment))) * 100000
            else:
                comment = int("".join(filter(str.isdigit, comment))) * 1000000
        elif comment.find("천") >= 0:
            if comment.find(".") >= 0:
                comment = int("".join(filter(str.isdigit, comment))) * 100
            else:
                comment = int("".join(filter(str.isdigit, comment))) * 1000
        else:
            comment = int("".join(filter(str.isdigit, comment)))

        # 게시물이 이미지인지 동영상인지 IGTV인지에 따라서 좋아요인가, 조회 수인가로 달라짐
        if image_video_igtv == 'image':
            image_love.append(love)
            image_comment.append(comment)
        elif image_video_igtv == 'video':
            video_love.append(love)
            video_comment.append(comment)
        elif image_video_igtv == 'igtv':
            igtv_love.append(love)
            igtv_comment.append(comment)

    lst = [len(image_love), len(image_comment), len(video_love), len(video_comment), len(igtv_love), len(igtv_comment)]
    # 나누기 0 예외처리
    for k in range(len(lst)):
        if lst[k] == 0:
            lst[k] = 1

    image_lmean = round(sum(image_love) / lst[0])
    image_cmean = round(sum(image_comment) / lst[1])
    video_lmean = round(sum(video_love) / lst[2])
    video_cmean = round(sum(video_comment) / lst[3])
    igtv_lmean = round(sum(igtv_love) / lst[4])
    igtv_cmean = round(sum(igtv_comment) / lst[5])

    temp = [account_link, image_lmean, image_cmean, video_lmean, video_cmean, igtv_lmean, igtv_cmean]
    print(account_link, image_lmean, image_cmean, video_lmean, video_cmean, igtv_lmean, igtv_cmean)
    box_list.append(temp)

print(len(box_list))
data = pd.DataFrame(box_list)
data.to_csv('beauty_influencer_post_info939.csv', encoding='utf-8-sig')

stop = timeit.default_timer()
print(stop - start)

driver.close()
