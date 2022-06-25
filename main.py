from pprint import pprint
import requests
import os

from yadisk import Yadisk
my_token = 'AQAAAABeVj3BAADLW2ETxduOYUAxlX3ukwhnvnA'

if __name__ == '__main__':
    yadisk = Yadisk(my_token)
    res = yadisk._get_upload_link('/file.txt')
    pprint(res)

    yadisk.upload_file('/test.txt','file.txt')

    res = yadisk._get_upload_link('/Tulips.jpg')
    pprint(res)
    yadisk.upload_file('/test_2.jpg', 'Tulips.jpg')