import sys
# My tokenize function's runtime is O(n)
# I run through the file once by checking if they are characters 
# then words
def tokenize(texts):
# I used the split method to check if file is

    termList = []
    term = ""
    
    for i in range(len(texts)):
        
        if (texts[i].isalnum()):
            termList.append(term)

            term+= texts[i].lower()
        elif not texts[i].isalnum():
            continue
        else:
            # this is used to check if length of word is 3 or more
            if (len(term)) >= 3:
                termList.append(term)
                term = ""
            else:
                term =""
    # this is used to check if length of # is 3 or more
    if (len(term)) > 3:
        termList.append(term)
    return termList

# My computeWordFrequencies function's runtime is O(n) time
# since I loop through the dictionary and checkup 
# each word O(1) time
def computeWordFrequencies(token):

# loops to check if token is already in dic then add one
# if token is not in dic add 1
    dict={}
    for i in token:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# My printMap function's runtime is O(n log n) time
# since I used the sorting which is O(n log n) 
def printMap(map: dict):

    maps=sorted(map, key=map.get, reverse=True)

    for i in maps:
        print(i,"=",map[i])

