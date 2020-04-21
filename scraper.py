import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    if resp.status >= 400 and resp.status <= 605:
        return list()

    #Implementation requred.
    #print("in extract_next_links")
    soup = BeautifulSoup(resp.raw_response.content, "lxml")

    seen = set()
    
    for link in soup.find_all('a'):
    # get absolute urls here before adding to listLInks()
        childURL = link.get('href')
        if is_valid(childURL):
            seen.add(childURL)  
            #print(childURL)

    for link in seen:
        print (link)
    return list(seen)


def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https", "today"]):
            return False
        if parsed.netloc not in set(["www.ics.uci.edu", "www.cs.uci.edu", "www.informatics.uci.edu", "www.stat.uci.edu", "today.uci.edu/department/information_computer_sciences"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise