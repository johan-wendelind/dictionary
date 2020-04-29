import json

from difflib import get_close_matches

data = json.load(open("data.json"))


def defineword(w):
    w = w.lower()
    c = w.capitalize()
    acronym = w.upper()
    if w and acronym in data:
        choise = input(
            f"Did you mean '{w}' or '{acronym}' Type '1' or '2': ").format()
        if choise == "1":
            return data[w]
        elif choise == "2":
            return data[acronym]
        else:
            return "We cant process that entry. Please try again."
    elif w in data:
        return data[w]
    elif c in data:
        return data[c]
    elif acronym in data:
        return data[acronym]
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

output = defineword(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
