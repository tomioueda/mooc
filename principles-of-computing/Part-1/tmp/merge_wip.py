"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    nonzeros_removed = []
    result = []
    merged = False

    # Remove zeroes from line
    for number in line:
        if number != 0:
            nonzeros_removed.append(number)

    # Fill line with zero's back to original length of line
    while len(nonzeros_removed) != len(line):
        nonzeros_removed.append(0)

    print nonzeros_removed
    
    for number in range(0, len(nonzeros_removed) - 1):
        if nonzeros_removed[number] == nonzeros_removed[number + 1]:
            if not merged:
                result.append(nonzeros_removed[number] * 2)
                merged = True
            elif nonzeros_removed[number] != nonzeros_removed[number + 1] and merged == False:
                result.append(nonzeros_removed[number])
            elif merged:
                merged = False
        elif nonzeros_removed[number] != nonzeros_removed[number + 1] and merged == False:
            result.append(nonzeros_removed[number])
        elif merged:
            merged = False

    if nonzeros_removed[-1] != 0:
        if not merged:
            result.append(nonzeros_removed[-1])

    while len(result) != len(nonzeros_removed):
        result.append(0)

    return result

if __name__ == '__main__':

    test_list = [0, 2, 0, 2]
    result = merge(test_list)
    # print result
    if result == [4, 0, 0, 0]:
        print "YAY\n"
    else:
        print "BOO\n"

    # test_list_b = [2, 2, 2, 2, 2]
    # result = merge(test_list_b)
    # print result
    # if result == [4, 4, 2, 0, 0]:
    #     print "YAY\n"
    # else:
    #     print "BOO\n"
