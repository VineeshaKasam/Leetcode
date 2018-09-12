'''
iven a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''
def isPalindrome(s):

    allchars = []
    for i in range(0,len(s)):
        if s[i].isalnum() == True:
            allchars.append(s[i])

    print allchars
    print len(allchars)
    bools = []
    print len(allchars)/2
    for k in range(0,(len(allchars)/2)):
        if allchars[k].lower() == allchars[len(allchars)-k-1].lower():
            print allchars[k], allchars[len(allchars)-k-1]
            bools.append(True)
        else:
            bools.append(False)

    print bools
    if False in bools:
        return 'false'
    else:
        return 'true'

print isPalindrome("A man, a plan, a canal: Panama")
print isPalindrome("race a car")


