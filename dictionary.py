import json

data = json.load(open("data.json"))
word = input("Type a singel english word to get the definition: ")
print(data["word"])
