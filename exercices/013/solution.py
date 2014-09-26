import sys

l = sys.argv

if len(l) > 1:
    print(l[1]) 
    
if len(l) == 1:
        print("usage: python3 solution.py PARAM")
