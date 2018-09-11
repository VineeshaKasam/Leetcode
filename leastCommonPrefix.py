
def lcp(strlist):
    lengths = [len(s) for s in strlist]
    min_len = min(lengths)
    lcp = ''
    for i in range(0,min_len):
        count = 0
        print i
        letter = strlist[0][i]
        letters = []
        for s in strlist:
            letters.append(s[i])
        for k in letters:
            if k==letter:
                count+=1
        if count==len(strlist):
            lcp+=letter

    for i in range(0,len(lcp)):
        all_chars = [s[i] for s in strlist]

        bools = [lcp[i]==charc for charc in all_chars]
        if False not in bools:
            return lcp
        else:
            return ''
    return lcp


print lcp(["flower","flow","flight"])
print lcp(["dog","racecar","car"])



