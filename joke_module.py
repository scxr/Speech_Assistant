from requests import get

def icanhazdad():
    headers = {'Accept': 'text/plain'}
    r = get('https://icanhazdadjoke.com/', headers=headers)
    if r.status_code == 200:
        return r.text


def chucknorris():
    r = get('https://api.chucknorris.io/jokes/random')
    if r.status_code == 200:
        return r.json()['value']
