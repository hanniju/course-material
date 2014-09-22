# S  = [a, b, c ,d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

S = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiouy'

for letter in reversed(S):
    if letter in vowels:
        print (letter.upper()),
    else:
        print (letter),

# 1 Avoid carriage return

# 2 = Write proper line synthax:
        # See 4.6.4 for lists: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# 3 =  How to sort vowels: https://www.daniweb.com/software-development/python/threads/175396/python-code-help-capitalize-only-vowels

# 4 = Reverse: http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
