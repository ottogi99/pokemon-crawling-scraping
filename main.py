import selenium
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.pokemonkorea.co.kr/pokedex")
driver.implicitly_wait(10)

# 스크롤 최하단으로 이동 (동적 컨텐츠)
# prev_height = driver.execute_script('return document.body.scrollHeight')
#
# while True:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     time.sleep(3)
#
#     current_height = driver.execute_script('return document.body.scrollHeight')
#
#     if prev_height == current_height:
#         break
#
#     prev_height = current_height
#
# time.sleep(3)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
# soup = BeautifulSoup(driver.page_source, 'lxml')

# thumbnails = soup.select_one('#\#pokedex_1 > a > div.img > div > img')
# thumbnails = soup.select('#\#pokedex_1 > a > div.img > div > img')
ul = soup.select_one('#pokedexlist')
li = ul.select('li')
# print(li)

for item in li:
    print(item.select_one('.tumb-wrp > img')['src'])    # 이미지 경로
    print(item.select_one('.bx-txt > h3').get_text())   # 전체
    print(item.select_one('.bx-txt > h3 > p').get_text())  # 번호
    num = item.select_one('.bx-txt > h3 > p').get_text()
    num_n_name = item.select_one('.bx-txt > h3').get_text()
    print(num_n_name.strip(num).strip())
    # print(item.select_one('.bx-txt > p'))
    print(item.select_one('.bx-txt > p').get_text().strip())    # 다른 모습
    # print()   # 이름
    spans = item.select('.bx-txt > span')
    for span in spans:
        print(span.get_text())

driver.quit()

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


