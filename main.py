from app import counries_iterator
from app import hash_generator

if __name__ == '__main__':

    countries = counries_iterator.CounryIterator('data/countries.json', 'data/wiki_links.txt')
    for item in countries:
        print(item)

    for gen_item in hash_generator.hash_gen('data/wiki_links.txt', 'data/hash.txt'):
        pass
    