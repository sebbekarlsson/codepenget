import requests
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema, ConnectionError


def get_code(codepen_url):
    code = {}

    try:
        res = requests.get(codepen_url)
    except (MissingSchema, ConnectionError):
        print('Invalid URL or ConnectionError')
        quit()

    if not res:
        print('Something went wrong')
        return None

    soup = BeautifulSoup(res.text, 'html.parser')
    blocks = soup.find_all('pre', {'class': 'code-box'})

    for block in blocks:
        code[block.get('id')] = block.find('code').text

    return code
