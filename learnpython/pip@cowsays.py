import cowsay
import sys
if len(sys.argv)==2:
    cowsay.trex("Hello," + sys.argv[1])
else:
    sys.exit("Usage: python cowsay.py [text]")