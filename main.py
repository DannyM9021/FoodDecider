from GUI import *
from decider import *
import random
def main():
    cond1 = welcome_page()
    results = submission_page(cond1)
    results_page(results)

main()