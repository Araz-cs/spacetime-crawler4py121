class DataBase:
    allTokens = dict()
    scraped = set()  # set of urls we've extracted from or are blacklisted
    seen = set()
    unique_urls = set()
    blacklistURL= set()

    @staticmethod
    def printList():
        f = open("URLS.txt", "a")

        for word in DataBase.scraped:
            f.write(word + "\n")

        f.write("\n\n\n\nUNIQUE URLS")

        for word in DataBase.unique_urls:
            f.write(word + "\n")

        f.close()

    def __init__(self):
        self.allTokens = dict()
        self.scraped = set()
        self.seen = set()
        self.unique_urls = set()
        self.blacklistURL = set()
