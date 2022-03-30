import time
from selenium import webdriver

from web_scraper.scraper import Scraper


class Crawler:
    def __init__(self):
        pass

    # Method 'crawling' may be 'static' --> 메소드 내부에서 self(객체의 인스턴스) 접근하는 로직이 없어서
    # Pycharm이 우리가 만든 메소드를 보고 얘가 지금 인스턴스가 필요하지 않은 static 메소드를 만드려고 하는건가?? 싶어서 띄우는 메시지입니다.
    def crawling(self, url, driver, time_to_wait=10, is_infinite_scroll=False, delay_to_scroll=3):
        driver = webdriver.Chrome() if driver is None else driver
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(time_to_wait)

        # 스크롤 최하단으로 이동 (동적 컨텐츠)
        if is_infinite_scroll:
            prev_height = driver.execute_script('return document.body.scrollHeight')

            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(delay_to_scroll)

                current_height = driver.execute_script('return document.body.scrollHeight')

                if prev_height == current_height:
                    break

                prev_height = current_height

            time.sleep(delay_to_scroll)

        scraper = Scraper(driver.page_source)
        parsed_items = scraper.parse()
        driver.quit()

        return parsed_items