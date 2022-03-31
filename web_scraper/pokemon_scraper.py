import os.path

from web_scraper.crawler import Crawler
from web_scraper.db_handler import DBHandler
from web_scraper.file_handler import FileHandler
from web_scraper.pokemon import PokeMon

if __name__ == '__main__':
    crawling_url = "https://www.pokemonkorea.co.kr/pokedex"
    pokemon_guide = []
    json_path = 'pokemon_guide.json'

    # 웹 Crawling 그리고 Scraping
    crawler = Crawler()
    parsed_items = crawler.crawling(crawling_url, is_infinite_scroll=True)

    for item in parsed_items:
        pokemon = PokeMon(item['number'], item['name'], item['mon_type'], thumbnail=item['thumbnail'])
        pokemon_guide.append(pokemon)

    # JSON 파일 저장
    FileHandler.pokemon_to_json(json_path, pokemon_guide)

    # JSON 파일 로딩
    pokemon_guide = FileHandler.json_to_pokemon(json_path)

    # 이미지 파일 로컬로 저장
    for pokemon in pokemon_guide:
        fileName = os.path.basename(pokemon.thumbnail)
        FileHandler.download_image(pokemon.thumbnail, f'thumbnail/{fileName}')
        print(f'Download is completed: {fileName}')

    exit(0)

    # JSON TO HEROKU DB로 저장
    db_handler = DBHandler()

    heroku_dbms = {
        'host': 'ec2-54-173-77-184.compute-1.amazonaws.com',
        'dbname': 'dejp68654rgcic',
        'user': 'xergwntdcrjmhl',
        'port': 5432,
        'password': '0c59bf14bbedfeba8e6ac2380898456de733b2abea0cbd6d408e138d751c4197'
    }

    db_handler.connect(
        host=heroku_dbms['host'],
        dbname=heroku_dbms['dbname'],
        port=heroku_dbms['port'],
        user=heroku_dbms['user'],
        password=heroku_dbms['password'],
    )

    columns = ['number', 'name', 'mon_type', 'height', 'weight', 'thumbnail', 'full_image']
    for pokemon in pokemon_guide:
        db_handler.insert(
            schema='public',
            table='illustrated_guide_illustratedguide',
            columns=','.join(columns),
            values=pokemon.to_values()
        )

        print('inserted completed!!')

    exit(0)
