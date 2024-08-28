from typing import Optional

import requests


def get_items(public_url: str) -> list:
    data = get_meta_data(public_url)
    return data.get('_embedded', {}).get('items', [])


def get_meta_data(public_url: str) -> Optional[dict]:
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_url}'
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None


def download_item(public_key: str, path: str) -> Optional[dict]:
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}'
    print(url)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None
