import json


# *args : arguments : 여러 개의 인자를 함수로 받고자 할 때 쓰입니다.
# 예시) 사람의 이름을 받아서 성과 이름을 분리한 후 출력
# 사용자가 '몇 개의' 이름을 적어 넣을지 알 수 가 없는 경우 *args를 인자로 받습니다.
def lastNameAndFirstName(*names):
    for name in names:
        print("%s %s" % (name[0], name[1:3]), end=' ')
    print('\n')

lastNameAndFirstName('정성화')
lastNameAndFirstName('정성화', '이승희')
lastNameAndFirstName('정성화', '이승희', '정율하')
lastNameAndFirstName('정성화', '이승희', '정율하', '정해슬')


## **kwargs : keyword argument : 특정 값 형태로 함수를 호출할 수 있습니다.
def introduceEnglishName(**kwargs):
    for key, value in kwargs.items():
        if 'ant' in kwargs.keys():
            print('주인님 오셨군요. 오늘 기분이 어떠세요?')
        else:
            print("{0} is {1}".format(key, value))

introduceEnglishName(MyName='Chris!!')
introduceEnglishName(ant='Chris!!')


def blog_printer(name, *blogs, **blog_benefits):
    '''
    :param name: 블로그 주인장의 이름
    :param blogs: 블로그를 만들 때 설명
    :param blog_benefits: 해당 블로그의 수익
    :return:
    '''

    print(name)
    print(blogs)
    print(blog_benefits)
    for post in blogs:
        print(post)
    for blog, benefits in blog_benefits.items():
        print(blog, '수익은 >>', benefits)

주인장이름 = '블로그 주인'
블로그1 = '첫번째 블로그지롱'
블로그2 = '성공해서 두번째 블로그도 만들었지롱'
블로그3 = '세번째도 만들었지롱'

help(blog_printer)
blog_printer(주인장이름, 블로그1, 블로그2, 블로그3, 블로그수익1=30, 블로그수익2=40, 블로그수익3=100)
