class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # initialize a random value in the array to res
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # if not in sorted order, compute the middle point
            m = (l + r) // 2
            res = min(res, nums[m])
            # decide to search left or right portion
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res