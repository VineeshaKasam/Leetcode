'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.
'''

def getPermutation(n, k):
    k = k - 1
    perm = ""
    nums = range(1, n + 1)
    while n > 0:
        n = n - 1
        idx, k = divmod(k, math.factorial(n))
        perm += str(nums[idx])
        nums.remove(nums[idx])

    return perm