"""
 https://en.wikipedia.org/wiki/Levenshtein_distance
 http://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm
"""

import numpy as np
import random
import string
def lev_dist(s, t):
    d = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]

    for i in range(len(t)+1):
        d[i][0] = i
    for i in range(len(s)+1):
        d[0][i] = i

    d[0][0] = 0
    
    for r in range(1, len(t)+1):
        for c in range(1, len(s)+1):
            if s[c-1] == t[r-1]:
                d[r][c] = d[r-1][c-1]
            else:
                d[r][c] = min(d[r-1][c-1]+1, d[r-1][c]+1, d[r][c-1]+1)

    print np.matrix(d)

    return d[len(t)][len(s)]

N = 500

t1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
t2 = t1[::-1]
print lev_dist(t1, t2)

t1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
t2 = t1+"2"
print lev_dist(t1, t2)

print lev_dist("XGYXYXYX", "XYXYXYTX")
print lev_dist("sitting", "kitten")
