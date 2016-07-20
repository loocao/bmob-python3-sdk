# encoding:utf-8
from bmob import Bmob

if __name__ == '__main__':
    bmob = Bmob(app_id='',
                rest_api_key='',
                secret_key='')
    file = open('hello.txt', 'rb')
    try:
        res = bmob.file.upload('hello.txt', file.read())
        print(res)
    finally:
        file.close()
