from spellchecker import SpellChecker # https://pyspellchecker.readthedocs.io/en/latest/

def spell_check(place:str) -> str:

    checker = SpellChecker()
    # find those words that may be misspelled
    lookup = checker.unknown([place])

    for word in lookup:
        # Get a list of `likely` options and returns the most likely
        return list(checker.candidates(word))[0]