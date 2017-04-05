# Palindrome Permutation: Given a string, write a function to check if
# it is a permutation of a palindrome A palindrome is a word or
# phrase that is the same  rwards and backwards. A permutation is a
#  rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

from collections import Counter


def is_palindrome_counter(data):
    data = Counter(data.replace(" ", "").lower())
    return sum(freq % 2 for freq in data.values()) < 2


print is_palindrome_counter("aa aa")
print is_palindrome_counter("Tact Coa")
print is_palindrome_counter("atco eta")
print is_palindrome_counter("abcba")
