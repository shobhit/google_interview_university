# Write a method to replace all spaces in a string with '%20
# You may assume that the string has suf cient space at the
#  end to hold the additional characters,and that you are given the
# "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this operation in place.)

a = "Shobhit  Jain"
s = ""
for i in a:
    if ord(i) == ord(" "):
        while ord(i) != ord(" "):
            continue
        s += "%20"
    else:
        s += i

print s

a = "Shobhit    Jain"
arr = list(a)
for i in range(len(arr)):
    if arr[i] == " ":
        arr[i] = "%20"

print "".join(arr)
