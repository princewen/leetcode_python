"""

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

"""

"""解题思路：http://www.th7.cn/Program/cp/201603/776061.shtml

考虑用动态规划法解决问题，因为当前日期买卖股票的行为会受到之前日期买卖股票行为影响。

对一天的状态有：buy买入，sell卖出，cooldown冷却。

但是对于这一天是否持股只有两种状态：持股状态（buy），没有持股状态（sell，cooldown）。

对于当天持股状态时，至当天的为止的最大利润有两种可能：1、今天没有买入，跟昨天持股状态一样；2、今天买入，昨天是冷却期，利润是前天卖出股票时候得到的利润减去今天股票的价钱。 二者取最大值。

对于当天未持股状态，至当天为止的最大利润有两种可能：1、今天没有卖出，跟昨天未持股状态一样；2、昨天持有股票，今天卖出了，利润是昨天持有股票时候的利润加上今天股票的价钱。 二者取最大值。

直至最后一天的状态应该是卖出状态。最终利润为sell[n-1];

状态转移方程：

sell[i] = max(sell[i-1], buy[i-1] + price[i]);

buy[i] = max(buy[i-1], sell[i-2] - price[i]);

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2 :
            return 0
        buy,sell,pre_buy,pre_sell = -prices[0],0,0,0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell-price,pre_buy)
            pre_sell = sell
            sell = max(pre_buy+price,pre_sell)
        return sell
