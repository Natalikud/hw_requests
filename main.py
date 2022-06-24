from pprint import pprint
import requests
import os

from yadisk import Yadisk
my_token = ''

if __name__ == '__main__':
    base_path = os.getcwd()
    my_file = 'file.txt'
    path = os.path.join(base_path, my_file)

    yadisk = Yadisk(my_token)

    yadisk.upload_file('/new/file.txt','file.txt')
