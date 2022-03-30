from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, page_source):
        self.page_source = page_source

    def parse(self, parser='html.parser'):
        soup = BeautifulSoup(self.page_source, parser)
        # soup = BeautifulSoup(driver.page_source, 'lxml')

        ul = soup.select_one('#pokedexlist')
        li = ul.select('li')

        result_list = []
        for item in li:
            thumbnail = item.select_one('.tumb-wrp > img')['src']
            number_name = item.select_one('.bx-txt > h3').get_text()
            number = item.select_one('.bx-txt > h3 > p').get_text()
            name = number_name.strip(number).strip()
            edition = item.select_one('.bx-txt > p').get_text().strip()
            # 진화
            evolution = ''
            # print()   # 이름
            # 타입
            spans = item.select('.bx-txt > span')
            mon_type_list = []
            for span in spans:
                mon_type_list.append(span.get_text())
            mon_type = '/'.join(mon_type_list)

            scraped_obj = {'thumbnail': thumbnail, 'number': number, 'name': name, 'mon_type': mon_type}
            result_list.append(scraped_obj)

        return result_list
