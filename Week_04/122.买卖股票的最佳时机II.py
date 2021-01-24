#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#使用贪心算法求解该题目
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #贪心算法
        local=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                local+=prices[i+1]-prices[i]
        return local
