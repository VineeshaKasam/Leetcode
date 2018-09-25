'''
Implement pow(x, n), which calculates x raised to the power n (xn).
'''

def myPow(self, x, n):

    if n == 0:
        return 1
    # if n==1:
    #     return x

    if n < 0:
        return 1 / self.myPow(x, -n)

    if n % 2 == 0:
        return self.myPow(x * x, n / 2)

    return x * self.myPow(x, n - 1)

