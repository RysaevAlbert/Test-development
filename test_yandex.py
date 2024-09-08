import requests
import pytest

class TestYaDisk:
    def setup_method(self):
        self.headers = {'Authorization': ''}


    def test_create_folder(self):
        params = {'path': 'image1'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 201


    def test_create_folder_again(self):
        params = {'path': 'image1'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 409

    def test_create_folder_author(self):
        params = {'path': 'image1'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=None,
                                params=params)
        assert response.status_code == 401

    def test_create_folder_data(self):
        params = {'path': None}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == 400