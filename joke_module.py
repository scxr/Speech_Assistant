from requests import get

def dad_joke():
    headers = {'Accept': 'text/plain'}
    r = get('https://icanhazdadjoke.com/', headers=headers)
    if r.status_code == 200:
        return r.text


def chuck_norris_joke():
    r = get('https://api.chucknorris.io/jokes/random')
    if r.status_code == 200:
        return r.json()['value']
