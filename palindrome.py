'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
def isPalindrome(x):
    if x < 0:
        return False
    copy, reverse = x, 0

    while copy:
        reverse *= 10
        reverse += copy % 10
        copy /= 10

    return x == reverse

print(isPalindrome(32123))