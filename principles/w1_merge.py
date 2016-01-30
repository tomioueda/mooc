"""
Merge function for 2048 game.
"""
import doctest

def merge(line):
    """
    Function that merges a single row or column in 2048.

    >>> merge([2, 0, 2, 4])
    [4, 4, 0, 0]
    >>> merge([0, 0, 2, 2])
    [4, 0, 0, 0]
    >>> merge([2, 2, 0, 0])
    [4, 0, 0, 0]
    >>> merge([2, 2, 2, 2, 2])
    [4, 4, 2, 0, 0]
    >>> merge([8, 16, 16, 8])
    [8, 32, 8, 0]

    """
    newline = []
    idx1 = 0
    while True:
        while idx1<len(line) and line[idx1]==0:
            idx1 +=1
        if idx1>=len(line):
            break
        idx2 = idx1 + 1
        while idx2<len(line) and line[idx2]==0:
            idx2 +=1
        if idx2>=len(line):
            newline.append(line[idx1])
            break
        if line[idx1]==line[idx2]:
            newline.append(2*line[idx1])
            idx1 = idx2+1
        else:
            newline.append(line[idx1])
            idx1 = idx2
    return newline + [0]*(len(line)-len(newline))

if __name__ == "__main__":

    doctest.testmod()
