'''
Given an input string, reverse the string word by word.
'''

def reverseWords(s):

    append_str = ""
    alist = []
    s = s.lstrip().rstrip()
    count = 0
    for i in range(0, len(s)):
        if s[i] == " ":
            if count == 1:
                continue
            if append_str!="": alist.append(append_str)
            append_str = ""
            count += 1

        if s[i]!=" ":
            append_str += s[i]
        count = 0

    alist.append(append_str)
    print alist

    return " ".join([word for word in reversed(alist)])

print reverseWords("the sky is blue")