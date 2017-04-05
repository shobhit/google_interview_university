# Given two strings,write a method to decide if one is a permutation of the
# other.


def nlognPerm(sample, sample1):
    if len(sample) != len(sample1):
        return "Invalid Strings"

    return sorted(sample) == sorted(sample1)


print nlognPerm("abc", "abc")

NUM_CHAR = 256


def nPerm(sample, sample1):
    if len(sample) != len(sample1):
        return False

    count1 = [0] * NUM_CHAR
    count2 = [0] * NUM_CHAR
    # print count1,count2

    for i, j in zip(list(sample), list(sample1)):
        count1[ord(i)] += 1
        count2[ord(j)] += 1

    for k in xrange(NUM_CHAR):
        if count1[k] != count2[k]:
            return False

    return True


print nPerm("abc", "bca")
print nPerm("abc", "bcad")
print nPerm("abc", "abc")
