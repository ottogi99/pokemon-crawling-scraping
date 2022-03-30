import json
import re
from enum import Enum
from json import JSONEncoder


class PokeMon(object):
    # slot을 통해 know attribute로 설정하면 메모리 사용양을 줄일 수 있다.
    __slots__ = ['number', 'name', 'monType', 'height', 'weight', 'thumbnail', 'fullImage']

    def __init__(self, number='', name='', monType=None, height=None, weight=None, thumbnail=None,
                 fullImage=None):
        self.number = number
        self.name = name
        self.monType = monType
        self.height = height
        self.weight = weight
        self.thumbnail = thumbnail
        self.fullImage = fullImage

    def __iter__(self):
        # yield from {
        #     "number": self.number,
        #     "name": self.name,
        #     "monType": self.monType,
        #     "height": self.height,
        #     "weight": self.weight,
        #     "thumbnail": self.thumbnail,
        #     "fullImage": self.fullImage
        # }.items()
        yield from {key: getattr(self, key, None) for key in self.__slots__}.items()

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    def to_dict(self):
        return dict(self)

    def to_json(self):
        return json.dumps(dict(self), indent=2, ensure_ascii=False)  # dict() 함수를 호출하면 객체내의 __iter__() 가 실행된다.

    def to_values(self):
        values = [self.number, self.name, self.monType, self.height, self.weight, self.thumbnail, self.fullImage]
        added_quotation_mark = ["''" if value is None else "'" + value + "'" for value in values]
        query_value_string = ','.join(added_quotation_mark)
        return query_value_string

    @staticmethod
    def from_json(json_dict):
        return PokeMon(json_dict['number'],
                       json_dict['name'],
                       json_dict['monType'],
                       json_dict['height'],
                       json_dict['weight'],
                       json_dict['thumbnail'],
                       json_dict['fullImage'])


def default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    raise TypeError(f'Object of type {obj.__class__.name__} is not JSON serializable')


if __name__ == '__main__':
    pokemon = PokeMon(1, '이상해씨')
    with open('pokemon_guide.json', 'w+', encoding='UTF-8') as fp:
        # normalized_json = re.sub(r'(?<!: )"(\S*?)"', '\\1', pokemon.to_json())
        fp.write(json.dumps(pokemon.to_json(), ensure_ascii=False))

    with open('pokemon_guide.json', 'r', encoding='UTF-8') as fp:
        pokemon_decoded = json.load(fp, object_hook=PokeMon.from_json)

    print(pokemon_decoded)
    exit(0)

    from json import JSONEncoder


    class MyEncoder(JSONEncoder):
        def default(self, obj):
            # return obj.to_json()
            return dict(obj)
            # return obj.__dict__


    pokemon = PokeMon(1, '이상해씨')
    print(pokemon)
    print(pokemon.to_json())
    # print(json.dumps(pokemon, default=default))
    # print(MyEncoder().encode(pokemon))
    # print(json.dumps(pokemon, cls=MyEncoder, ensure_ascii=False))
    # print(pokemon)
    # print(pokemon)
    # print(json.dumps(pokemon.__dict__))
