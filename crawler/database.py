class DataBase:
    allTokens = dict()
    scraped = set()  # set of urls we've extracted from or are blacklisted
    seen = set()
    unique_urls = set()
    blacklistURL= set()
    maxWords = ["", 0] # maxWords[0] is URL, maxWords[1] is number of words

    @staticmethod
    def printList():
        f = open("URLS.txt", "a")

        for word in DataBase.scraped:
            f.write(word + "\n")

        f.write("\n\n\n\nUNIQUE URLS")

        for word in DataBase.unique_urls:
            f.write(word + "\n")

        f.write("\n\n\n\nBLACKLISTED URLS\n")
        for word in DataBase.blacklistURL:
            f.write(word + "\n")

        f.write("\n\n\n\nLONGEST PAGE(IN TERMS OF NUMBER OF WORDS)\n")
        f.write("Website URL: " + str(DataBase.maxWords[0]) + "\n")
        f.write("Number of words: " + str(DataBase.maxWords[1]) + "\n")

        f.close()

    def __init__(self):
        self.allTokens = dict()
        self.scraped = set()
        self.seen = set()
        self.unique_urls = set()
        self.blacklistURL = set()
        self.maxWords = ["", 0]
