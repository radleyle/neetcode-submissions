class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # res = 0

        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heighs[r]) # we get the high by taking the bottle neck between the 2 heights, take whichever one is lower
        #         res = max(res, area)

        # return res

        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                r -= 1 # since they're equal, shifting either left or right pointer doesn't matter. Then, we can opt to remove the condition elif and just keep the else condition.

        return res

