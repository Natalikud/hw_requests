from pprint import pprint
import requests
import os


class Yadisk:

    def __init__(self, token):
        self.token = token
        self.host = 'https://cloud-api.yandex.net:443'
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth{self.token}'
                        }

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resourses/upload/'
        headers = self.headers
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        pprint(f'{url},{params},{headers}')
        return response.json().get('href')

    def upload_link(self, file_name: str):
        upload_link = self._get_upload_link(path_to_file)
        headers = self.headers
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)

        response.raise_for_status()
        if response.status_code == 201:
            print('Sucsess')


if __name__ == '__main__':
    my_token = ''
    base_path = os.getcwd()
    my_file = 'file.txt'
    path_to_file = os.path.join(base_path, my_file)

    yadisk = Yadisk(my_token)
    yadisk.upload_link(path_to_file)
