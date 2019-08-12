"""
Medium

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

# 三个状态 buy sell rest, 之间互相转移，维护3个dp数组
# hold[i] = max(hold[i-1], rest[i-1] - prices[i])
# sold[i] = hold[i-1] + prices[i]
# rest[i] = max(rest[i-1], sold[i-1])   // max()内不考虑 hold[i-1],其一定小于rest[i-1], 即买了不卖不如不买
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy, pre_buy, sell, pre_sell = -max(prices), 0, 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
        return sell

"""
剔除冗余，三个状态转换 变为两个：
hold = max(sold(i-2)-prices[i], hold[i-1])
sold = max(hold[i-1]+prices[i], sold[i-1])
"""