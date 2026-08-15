class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = buy, right = sell
        maxP = 0

        while r < len(prices):
            # check if its a profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # check if the current profit is better than the max profit and update
            else:
                l = r # if the buy pricess >= sell price, we shift it all the way to the right, since we found the minimum price 
            r += 1

        return maxP
