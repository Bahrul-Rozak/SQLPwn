import requests
import time
from urllib.parse import urljoin, urlparse
from colorama import Fore

class RequestHelper:
    def __init__(self, timeout=10, delay=0):
        self.session = requests.Session()
        self.timeout = timeout
        self.delay = delay
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def send_get(self, url, params=None):
        try:
            if self.delay > 0:
                time.sleep(self.delay)
            
            response = self.session.get(
                url, 
                params=params, 
                timeout=self.timeout,
                verify=False,
                allow_redirects=True
            )
            return response
        except requests.exceptions.RequestException as e:
            return None
    
    def send_post(self, url, data=None):
        try:
            if self.delay > 0:
                time.sleep(self.delay)
            
            response = self.session.post(
                url,
                data=data,
                timeout=self.timeout,
                verify=False,
                allow_redirects=True
            )
            return response
        except requests.exceptions.RequestException as e:
            return None
    
    @staticmethod
    def extract_forms(html_content):
        from bs4 import BeautifulSoup
        forms = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        for form in soup.find_all('form'):
            form_details = {
                'action': form.get('action', ''),
                'method': form.get('method', 'get').lower(),
                'inputs': []
            }
            
            for input_tag in form.find_all('input'):
                input_details = {
                    'name': input_tag.get('name', ''),
                    'type': input_tag.get('type', 'text'),
                    'value': input_tag.get('value', '')
                }
                form_details['inputs'].append(input_details)
            
            forms.append(form_details)
        
        return forms