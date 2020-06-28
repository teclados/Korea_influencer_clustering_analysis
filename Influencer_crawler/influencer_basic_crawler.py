from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium import webdriver
import timeit

# 본격 크롤링 시작
# Try & error 주석처리
# beauty_influencer_account.csv 를 바탕으로 basic info 수집
# 인스타그램 일정 access 량 초과로 인해 여러 계정으로 여러번 시도해야 함.

driver = webdriver.Chrome('C:/Users/aaa/Downloads/chromedriver_win32/chromedriver.exe')
# 인스타 로그인
url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)
time.sleep(4)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
    "아이디")
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(
    "비밀번호")
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
time.sleep(3)

# ---------------------------------------------------------------------

start = timeit.default_timer()

beauty_data = pd.read_csv('./beauty_influencer_account.csv')
box_list = list()
for j in range(970, 1000):
    i = beauty_data['0'][j]
    driver.get(i)
    time.sleep(1.0)
    pageString1 = driver.page_source
    bsObj1 = bs(pageString1, 'html.parser')
    check_error = bsObj1.select('body > div > form')
    if len(check_error) == 0:
        error_account = [i, -1, -1, -1, -1, -1]
        print(error_account)
        box_list.append(error_account)
        continue

    # 공식 계정 유무
    official_obj = bsObj1.select('.nZSzR > span')
    official = 1
    if len(official_obj) == 0:
        official = 0

    # 기본    정보 추출
    boxs = bsObj1.select('.k9GMp > .Y8-fY')
    # post 수
    post_num = boxs[0].find('a').find('span').text
    post = int("".join(filter(str.isdigit, post_num)))

    # follower 수, 공개 계정 유무
    open_yes = 1
    follower_num = boxs[1].find('a')
    if str(type(follower_num)) == "<class 'NoneType'>":
        follower_num = boxs[1].find('span').find('span')['title']
        open_yes = 0
    else:
        follower_num = follower_num.find('span')['title']
    follower = int("".join(filter(str.isdigit, follower_num)))

    # follow 수
    follow_num = boxs[2].find('a')
    if str(type(follow_num)) == "<class 'NoneType'>":
        follow_num = boxs[2].find('span').find('span').text
        if follow_num.find("백만") >= 0 or follow_num.find("천") >= 0:
            follow_num = -1  # 다시 확인하기
        else:
            follow_num = int("".join(filter(str.isdigit, follow_num)))
    else:
        follow_num = follow_num.find('span').text
        if follow_num.find("백만") >= 0 or follow_num.find("천") >= 0:
            follow_num = -1  # 다시 확인하기
        else:
            follow_num = int("".join(filter(str.isdigit, follow_num)))

    temp = [i, post, follower, follow_num, open_yes, official]
    print(temp)
    box_list.append(temp)

print(len(box_list))

data = pd.DataFrame(box_list)
data.to_csv('beauty_influencer_basic_info1000ex.csv', encoding='utf-8-sig')

stop = timeit.default_timer()
print(stop - start)

driver.close()

# ----------------------추가적인 참고 코드 (시행착오)-------------------------

# # -------------------(1)인스타그램 hover 속성 활용--------------------------
#
# start = timeit.default_timer()
# post_set = set()
# temp_set = set()
# current_set = set()
# pagedown = 0.7
# while True:
#     pageString = driver.page_source
#     bsObj = bs(pageString, "html.parser")
#     bs_list = bsObj.select(".v1Nh3")
#     temp_set.clear()
#     print(type(bs_list))
#
#     if len(current_set) == 0:
#         for popular in bs_list:
#             current_set.add(popular)
#     else:
#         for popular in bs_list:
#             temp_set.add(popular)
#         current_set = temp_set - current_set
#
#     for popular in current_set:
#         p_link = popular.find('a')['href']
#         # 게시물 hover instance 가져오기
#         try:
#             hove = driver.find_element_by_xpath(
#                 "//div[@class='Nnq7C weEfm']/div[@class='v1Nh3 kIKUG  _bz0w']/a[@href='{}']".format(p_link))
#             action = ActionChains(driver)
#             action.move_to_element(hove).perform()
#             time.sleep(0.3)
#             pageString2 = driver.page_source
#             bsObj2 = bs(pageString2, "html.parser")
#             bs_list2 = bsObj2.select("div.qn-0x > ul > li > span")
#             # hover 예외처리
#             if len(bs_list2) == 0:
#                 continue
#             # 좋아요 수 예외처리
#             love = bs_list2[0].text
#             if love.find("백만") >= 0:
#                 if love.find(".") >= 0:
#                     love = int("".join(filter(str.isdigit, love))) * 100000
#                 else:
#                     love = int("".join(filter(str.isdigit, love))) * 1000000
#             elif love.find("천") >= 0:
#                 if love.find(".") >= 0:
#                     love = int("".join(filter(str.isdigit, love))) * 100
#                 else:
#                     love = int("".join(filter(str.isdigit, love))) * 1000
#             else:
#                 love = int("".join(filter(str.isdigit, love)))
#             print(love)  # 확인용
#
#             if love > 100:
#                 print('*' + str(love))  # 확인용
#                 post_set.add(p_link)
#         except NoSuchElementException:
#             print('except: ' + str(p_link))
#             continue
#     print('once: ' + str(len(post_set)))  # 확인용

# # ------------------------비디오 조회수 예외처리-------------------------------
# temp_v = bsObj1.select('.vcOH2')
#
#     for video in temp_v:
#         temp_view = video.find('span')
#         if str(type(temp_view)) == "<class 'NoneType'>":
#             print("none")
#             continue
#         temp_view = temp_view.text
#         temp_view = int("".join(filter(str.isdigit, temp_view)))
#         if int(temp_view) > 1000:
#             for s in temp_a:
#                 temp1_t = s.find('a')['href']
#                 pop_link = 'https://www.instagram.com' + temp1_t
#                 middle = timeit.default_timer()
#                 print(pop_link)
#                 print('middle time: ' + str(middle - start))
#                 account_set.add(pop_link)
# -------------------------스크롤 체크포인트--------------------------------------
# post_set = set()
# pagedown = 1.0
# pagedown2 = 1.0
# checkpoint = 0
# checkpoint2 = 0
# for i in range(198):  # range 안에 checkpoint
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(pagedown2)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     checkpoint2 += 1
#     if new_height == last_height:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(pagedown2)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         else:
#             last_height = new_height
#             time.sleep(pagedown2)
#             continue
#
# print(checkpoint2)
#
# time.sleep(3)
# # --------------------------스크롤------------------------------------------
#
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(pagedown)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(pagedown)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         else:
#             last_height = new_height
#             continue
#
# # --------------------------------------------------------------
#
# print(len(post_set))
# post_lst = list(post_set)
#
# # account_set = set()
# #
# # for i in range(len(post_lst)):
# #     post_link = 'https://www.instagram.com' + post_lst[i]
# #     driver.get(post_link)
# #     time.sleep(0.1)
# #     pageString1 = driver.page_source
# #     bsObj1 = bs(pageString1, 'html.parser')
# #     temp = bsObj1.select('.Nm9Fw')
# #     temp1 = bsObj1.select('.e1e1d')
# #     for k in temp:
# #         temp_t = k.find('span')
# #         if str(type(temp_t)) == "<class 'NoneType'>":
# #             continue
# #         temp_t = temp_t.text
# #         if int(temp_t) > 500:
# #             for s in temp1:
# #                 temp1_t = s.find('a')['href']
# #                 pop_link = 'https://www.instagram.com' + temp1_t
# #                 account_set.add(pop_link)
# #
# # account_lst = list(account_set)
# # print(len(account_lst))
# # result = list()
# # for i in range(len(account_lst)):
# #     popular_account = account_lst[i]
# #     in_result = [popular_account]
# #     result.append(in_result)
# #
# # data = pd.DataFrame(result)
# # data.to_csv('popular_influencer.csv', encoding='utf-8-sig')
#
# stop = timeit.default_timer()
# print(stop - start)
#
# driver.close()
