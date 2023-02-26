from GUI import *
#from decider import *
def main():
    cond1 = welcome_page()
    results = list(submission_page(cond1).values())
    print(results)


main()