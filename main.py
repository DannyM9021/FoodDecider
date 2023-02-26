from GUI import *
from decider import *
def main():
    cond1 = welcome_page()
    results = submission_page(cond1)
    if results is not None:
        searching(list(results.values()))


main()