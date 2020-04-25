import re
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment

lower_bound = 3000
upper_bound = 150000

def check_characters():
    url = "https://wics.ics.uci.edu/events/category/volunteer-opportunity/1991-06-08/"
    html = urlopen(url)
    print (url)
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(text=lambda text: isinstance(text,Comment)):
        tag.extract()

    for element in soup.findAll(['script', 'style']):
        element.extract()

    #this is what to send to the tokenizer
    webtext = soup.get_text()

    space_delemited_text = re.sub('\s+',' ',webtext)

    print(len(space_delemited_text)) 

if __name__ == "__main__":
    check_characters()