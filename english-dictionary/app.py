import json
import difflib

data = json.load(open("english-dictionary/data.json"))


def getDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        similar = difflib.get_close_matches(word, data.keys())
        if len(similar) > 0:
            return "Did you mean '{}'? Try again:".format(similar[0])
        else:
            return "The word '{}' does not exist. Try another word:".format(word)


print(
    "WELCOME TO THE ENGLISH DICTIONARY PROGRAM. ENTER A WORD BELOW TO RETREIVE IT'S DEFINITION\n"
)
print("====================================================================\n")
word = input("Enter a word: ")
definitions = getDefinition(word)
while not isinstance(definitions, list):
    word = input("{} ".format(definitions))
    definitions = getDefinition(word)

print("\nDefinition of '{}':".format(word))
for d in definitions:
    print(f"{d}")

input("\nPress any key to exit...")
