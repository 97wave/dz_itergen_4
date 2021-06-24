import requests
import json
from bs4 import BeautifulSoup

class CounryIterator:
    
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        with open (self.input_path, encoding='utf-8') as f:
            self.data = json.load(f)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        
        self.country_name =  self.data[self.index]['name']['common']

        resp = requests.get('http://ru.wikipedia.org/?action=opensearch&search=' + self.country_name + '&limit=1&prop=info&format=xml&inprop=url')
        soup = BeautifulSoup(resp.text, 'html.parser')
        link_tag = soup.find("link", rel = "canonical")
        link = link_tag.get('href')

        string = self.country_name + " - " + link + '\n'
        with open (self.output_path, 'a', encoding='utf-8') as f:
            f.write(string)

        self.index += 1
        return self.index