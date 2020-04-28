from crawler.database import DataBase as d

# utils.py



# tokenize function's runtime is O(n)
def tokenize(url, texts):
# I used the split method to check if file is

    termList = []
    term = ""

    for i in range(len(texts)):
        if (texts[i].isalnum()):
            term += texts[i].lower()
        # elif not texts[i].isalnum():
        #     continue
        else:
            # this is used to check if length of word is 3 or more
            if (len(term)) >= 3:
                termList.append(term)
                term = ""
            else:
                term =""

    # loops to check if token is already in dic then add one
    # if token is not in dic add 1
    for i in termList:
        if i in d.allTokens:
            d.allTokens[i] += 1
        else:
            d.allTokens[i] = 1


    # checks if it has more words than the current maximum
    if len(termList) > d.maxWords[1]:
        d.maxWords[0] = url
        d.maxWords[1] = len(termList)
        

stopWords = {"a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
"before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
"during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's",
"hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more",
"most","mustn't","my","myself","no""nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same",
"shan't","she","she'd","she'll","she's","should","shouldn'tso","some","such","than","that","that's","the","their","theirs","them","themselves","then","there",
"there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we",
"we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with",
"won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"}

# This function answers problem 3, and writes it to a file.
def problem3():
    f = open("P3wordlist.txt", "w+")
    counter = 0
    for k, v in sorted(d.allTokens.items(), key = lambda x: -x[1]):
        if k not in stopWords:
            f.write(k + "=" + str(v))
            f.write("\n")
            counter += 1
        if counter == 70:
            break
    f.close()
