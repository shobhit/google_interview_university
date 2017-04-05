# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
import sys


def n2getuniq(sample1):
    for i in range(len(sample1)):
        for j in range(i + 1, len(sample1)):
            # print sample1[i], sample1[j]
            if sample1[i] == sample1[j]:
                print "Not Unique", sample1
                return
    print "Unique String", sample1


n2getuniq("abcd")
n2getuniq("adbca")


def nlognsorteduniq(sample):
    n = sorted(sample)
    prev = None
    for i in n:
        if i == prev:
            print "Not Unique"
            return
        prev = i
    print "Unique"
    return


nlognsorteduniq("abcd")
nlognsorteduniq("abcdd")


# OPTION 5: bitwise attempt
# only consider lowercase character a-z, which fits in 4 bytes.
# Time: O(n)   Space: O(1) => 4 bytes.
def unique_characters_bitwise(input_string):
    if len(input_string) > 26:
        return False
    # each bit represents the presence of a character or not (e.g. bit position 0 represents 'a')
    check_bytes = 0
    for char in input_string:
        idx = ord(char) - ord('a')
        print idx
        print 1 << idx
        if (check_bytes & (1 << idx)) > 0:
            return False
        check_bytes = check_bytes | (1 << idx)
    return True


print unique_characters_bitwise("abcd")
