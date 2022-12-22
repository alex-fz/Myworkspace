#!/usr/bin/env python3

from urllib import request
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import re

### Use a thread per url, store the html in a dict as the value and the key the name of the page

def collect_info(urls):
    with request.urlopen(urls) as my_opener:
        reader = my_opener.read()
        my_soup = BeautifulSoup(reader, features="html.parser")
    
    my_opener.close()
    return my_soup

my_urls = ['https://webscraper.io/test-sites/e-commerce/allinone', 'https://www.amazon.es/', 'https://open.spotify.com/']


# por cada url sera un thread
my_pool = Pool(len(my_urls)*2)
the_return = my_pool.map(collect_info, my_urls)
# cerrar el pool y esperar a que finalice
my_pool.close()
my_pool.join()

dict_of_webs = {}
for i,v in enumerate(the_return):
    str_to_replace = v.find('title').string
    str_to_replace = re.sub(r'(\s.*)', '', str_to_replace)
    dict_of_webs[str_to_replace] = v

print(dict_of_webs.keys())