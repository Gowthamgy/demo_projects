import requests
import json
import os


def extract_data():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    data = response.json()
    return data