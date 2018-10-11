def nextPermutation(nums):
    # find longest non-increasing suffix
    right = len(nums) - 1
    while nums[right] <= nums[right - 1] and right - 1 >= 0:
        right -= 1
    if right == 0:
        return reverse(nums, 0, len(nums) - 1)
    # find pivot
    pivot = right - 1
    successor = 0

    # find rightmost succesor
    for i in range(len(nums) - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            successor = i
            break
    # swap pivot and successor
    # print pivot
    # print successor

    nums[pivot], nums[successor] = nums[successor], nums[pivot]
    # reverse suffix
    reverse(nums, pivot + 1, len(nums) - 1)


def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

print nextPermutation([3,2,1])