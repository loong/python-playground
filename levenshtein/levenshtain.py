"""
 https://en.wikipedia.org/wiki/Levenshtein_distance
 http://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm
"""

import numpy as np

def lev_dist(s, t):
    d = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]

    for i in range(len(t)+1):
        d[i][0] = len(s)
    for i in range(len(s)+1):
        d[0][i] = len(t)

    d[0][0] = 0
    
    for r in range(1, len(t)+1):
        for c in range(1, len(s)+1):
            if s[c-1] == t[r-1]:
                d[r][c] = d[r-1][c-1]
            else:
                d[r][c] = min(d[r-1][c-1]+1, d[r-1][c]+1, d[r][c-1]+1)

    print np.matrix(d)

    return d[len(t)][len(s)]

print lev_dist("kitten", "sitting")
