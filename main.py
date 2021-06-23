import requests
import json
from bs4 import BeautifulSoup

from pprint import pprint

from Lib import hashlib


class CounryIterator:
    
    def __init__(self, countries_json_path):
        self.countries_json_path = countries_json_path
        with open (self.countries_json_path, encoding='utf-8') as f:
            self.data = json.load(f)
        self.index = 0
        self.index_end = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.index_end:
            raise StopIteration
        
        self.country = self.data[self.index]
        self.country_name =  self.data[self.index]['name']['common']

        resp = requests.get('http://ru.wikipedia.org/?action=opensearch&search=' + self.country_name + '&limit=1&prop=info&format=xml&inprop=url')
        soup = BeautifulSoup(resp.text, 'html.parser')
        link_tag = soup.find("link", rel = "canonical")
        link = link_tag.get('href')
        
        if link[25]  == '?':
            # link = 'https://ru.wikipedia.org/wiki/'
            pass

        string = self.country_name + " - " + link + '\n'

        with open ('wiki_links.txt', 'a', encoding='utf-8') as f:
            f.write(string)

        self.index += 1
        return self.index


def hash_generator(start=0):
    with open ('wiki_links.txt', 'r') as wiki:
        with open ('md.txt', 'a') as md:
            strings = wiki.readlines()
            while start < len(strings):
                string = strings[start]
                hash_object = hashlib.md5(string.encode())
                md.write(hash_object.hexdigest())
            yield start
            start += 1

if __name__ == 'main.py':
    countries = CounryIterator('countries.json')

    # for item in countries:
    #     pprint(item)

    for item_gen in hash_generator():
        print('g' + item_gen)


