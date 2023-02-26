from GUI import *
from decider import *
import random
def main():
    cond1 = welcome_page()
    results = submission_page(cond1)
    if results is not None:
        places = searching(list(results.values()))
        rng = random.randint(0, len(places)-1)
        print(places[rng][1])

main()