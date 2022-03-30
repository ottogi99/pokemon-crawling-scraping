import json
import dload

from web_scraper.pokemon import PokeMon


class FileHandler:
    @staticmethod
    def pokemon_to_json(path, pokemon_list_obj):
        # 파일저장 부분
        with open(path, 'w', encoding='UTF-8') as f:
            json_obj_list = []
            for pokemon_obj in pokemon_list_obj:
                json_obj = pokemon_obj.to_dict()
                json_obj_list.append(json_obj)

            try:
                f.write(json.dumps(json_obj_list, indent=4, ensure_ascii=False))
            except OSError:
                print("Could not write file: %s" % path)
                pass

    @staticmethod
    def json_to_pokemon(path):
        with open(path, 'r', encoding='UTF-8') as f:
            return json.load(f, object_hook=PokeMon.from_json)

    @staticmethod
    def download_image(image_url, download_path):
        dload.save(image_url, download_path)
