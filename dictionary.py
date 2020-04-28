import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def defineword(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y or N: " %
                   get_close_matches(w, data.keys(), cutoff=0)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "Word does not exist"
        else:
            return "We didn't undrstand your entry."
    else:
        return "Word does not exist"


word = input("Type a singel english word to get the definition: ")

print(defineword(word.lower()))
