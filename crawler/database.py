class DataBase:
    allTokens = dict()
    scraped = set()  # set of urls we've extracted from or are blacklisted
    seen = set()
    unique_urls = set()


    def __init__(self):
        self.allTokens = dict()
        self.scraped = set()
        self.seen = set()
        self.unique_urls = set()
        
