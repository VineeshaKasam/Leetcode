'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def climbStairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)

print climbStairs(20)