import requests

# Задача №2
# Написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Я.Диск с таким же именем.
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # Загрузка одного файла:
    def upload(self, file_path: str, single_file: str):
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        link = requests.get(upload_url, headers=headers, params=params).json()
        url = link.get("href", "")
        response = requests.put(url, data=open(single_file, 'rb'))
        response.raise_for_status()

    # Загрузка списка файлов:
    def upload_list(self, file_path: str, file_list):
        for i, file_name in enumerate(file_list):
            path_to_list = f'{file_path}/{file_name}'
            headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {"path": path_to_list, "overwrite": "true"}
            link = requests.get(upload_url, headers=headers, params=params).json()
            url = link.get("href", "")
            response = requests.put(url, data=open(file_name, 'rb'))
            response.raise_for_status()


if __name__ == '__main__':
    token = input('Введите token: ')
    uploader = YaUploader(token)
    catalog_name = input('Название папки, куда загрузить файлы: ')


    # Загрузка списка файлов:
    file_list = []
    result_list_uploader = uploader.upload_list(catalog_name, file_list)

    # Загрузка одного файла:
    file_name = ''
    path_to_file = f"{catalog_name}/{file_name}"
    result_single_uploader = uploader.upload(path_to_file, file_name)