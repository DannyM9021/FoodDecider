from spellchecker import SpellChecker # https://pyspellchecker.readthedocs.io/en/latest/

def spell_check(place):

    checker = SpellChecker()
    # find those words that may be misspelled
    lookup = checker.unknown([place])

    for word in lookup:
        # Get a list of `likely` options
        return checker.candidates(word)

def main():
    place = spell_check(input("Where do you want to eat? "))
    print(place)
main()