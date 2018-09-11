'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''

def addBinary(a, b):
    a = list(a)
    b = list(b)

    result = []
    carry = 0
    while len(a)>0 or len(b)>0:

        print a,b
        k1=k2=0
        if a : k1 = int(a.pop())
        if b: k2 = int(b.pop())

        sum_val = k1 + k2 + carry

        carry=0

        if sum_val in [0,1]:
            result.append(sum_val)
        elif sum_val==2:
            result.append(0)
            carry+=1
        else:
            result.append(1)
            carry+=1

    if carry:
        result.append(carry)

    return "".join(str(i) for i in result)[::-1]

print addBinary("11", "1")

