import sys
def vote():
    num="18"
    if sys.argv[1]==num:
        sys.exit("You are eligible to vote")
    else:
        sys.exit("You are not eligible to vote")
vote()

