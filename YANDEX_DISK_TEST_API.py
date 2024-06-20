import requests
import unittest
import time # Добавил КД, чтобы ждать когда папка удалится точно, без этого падало с ошибкой что папка еще существует
            # При массовой обработке файлов и папок, это может замедлить работу, но для теста пусть будет, сделал специально


class TestYandexDiskAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        cls.token = 'ТОКЕН' # свой я здесь палить не буду. Ни здесь ни в .env 
        cls.headers = {
            'Authorization': f'OAuth {cls.token}'
        }
        cls.folder_path = 'disk:/test_folder'
        cls.delete_folder()

    @classmethod
    def delete_folder(cls):
        params = {'path': cls.folder_path, 'permanently': True}
        response = requests.delete(cls.base_url, headers=cls.headers, params=params)
        print(f"Delete folder response: {response.status_code}, {response.text}")
        if response.status_code == 202:  # Accepted, удаление выполняется
            while True:
                response = requests.get(cls.base_url, headers=cls.headers, params=params)
                if response.status_code == 404:  # Not Found, папка удалена
                    break
                time.sleep(1)

    def test_create_folder_success(self):
        self.delete_folder()  # Удаляем папку перед началом теста
        params = {'path': self.folder_path}
        response = requests.put(self.base_url, headers=self.headers, params=params)

        print(f"Create folder response: {response.status_code}, {response.text}")

        self.assertEqual(response.status_code, 201, "Expected status code 201 for folder creation")

        response = requests.get(self.base_url, headers=self.headers, params=params)
        print(f"Check folder response: {response.status_code}, {response.text}")

        self.assertEqual(response.status_code, 200, "Expected status code 200 for folder existence")
        self.assertIn('resource_id', response.json(), "Folder should have a resource_id")

    def test_create_folder_already_exists(self):
        params = {'path': self.folder_path}
        response = requests.put(self.base_url, headers=self.headers, params=params)
        print(f"First create folder response: {response.status_code}, {response.text}")
        response = requests.put(self.base_url, headers=self.headers, params=params)
        print(f"Second create folder response: {response.status_code}, {response.text}")

        self.assertEqual(response.status_code, 409, "Expected status code 409 for folder already exists")

    def test_create_folder_invalid_token(self):
        invalid_headers = {
            'Authorization': 'OAuth INVALID_TOKEN'
        }
        params = {'path': self.folder_path}
        response = requests.put(self.base_url, headers=invalid_headers, params=params)
        print(f"Invalid token response: {response.status_code}, {response.text}")

        self.assertEqual(response.status_code, 401, "Expected status code 401 for invalid token")

    def test_create_folder_invalid_path(self):
        invalid_folder_path = 'disk:/<invalid_folder>'
        params = {'path': invalid_folder_path}
        response = requests.put(self.base_url, headers=self.headers, params=params)
        print(f"Invalid path response: {response.status_code}, {response.text}")

        self.assertEqual(response.status_code, 409, "Expected status code 409 for invalid path")

    @classmethod
    def tearDownClass(cls):
        cls.delete_folder()


if __name__ == '__main__':
    unittest.main()
