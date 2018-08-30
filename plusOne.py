'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
'''

def plusOne(    digits):
    theint = int("".join([str(i) for i in digits])) + 1

    new_list = []
    for k in range(0, len(str(theint))):
        new_list.append(int(str(theint)[k]))

    return new_list

print(plusOne([4,3,2]))
print(plusOne([0]))