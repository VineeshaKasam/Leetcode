'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
=(i.e., buy one and sell one share of the stock multiple times).
'''

def maxProfit(prices):
    return sum([max(prices[i + 1] - prices[i], 0) for i in range(0, len(prices) - 1)])

print maxProfit([7,1,5,3,6,4])
