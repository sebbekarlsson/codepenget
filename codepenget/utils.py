import requests
from bs4 import BeautifulSoup


def get_code(codepen_url):
    code = {}
    res = requests.get(codepen_url)

    if not res:
        return None

    soup = BeautifulSoup(res.text, 'html.parser')
    blocks = soup.find_all('pre', {'class': 'code-box'})

    for block in blocks:
        code[block.get('id')] = block.find('code').text

    return code
