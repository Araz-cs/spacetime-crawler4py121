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
    dict={}
    for i in termList:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict



if __name__ == "__main__":
    text = "WOLF, meeting with a Lamb astray from the fold, resolved not to\
    lay violent hands on him, but to find !! some plea {{to justify to the\
    Lamb the Wolf's right to $$$eat him.  He thus addressed him:"
    x = tokenize(text)
    print(x)
