import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, file_path_load: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": file_path_load, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("файл загружен!")

if __name__ == '__main__':
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    path_to_file = input('Введите путь к файлу: ')
    path_to_load = input('Введите путь загрузки: ')
    result = uploader.upload(path_to_file, path_to_load )