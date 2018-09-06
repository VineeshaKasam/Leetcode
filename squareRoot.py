'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
'''


def sqrtX(x):
    l = 0
    r = x
    while l<=r:
        mid = (l+r)//2
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid*mid:
            r = mid
        else:
            l = mid+1


print sqrtX(8)
