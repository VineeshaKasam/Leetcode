class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return True

            # to avoid duplicates in the right and left parts of mid
            while low < mid and nums[mid] == nums[low]:
                low += 1
            while high > mid and nums[mid] == nums[high]:
                high -= 1

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False