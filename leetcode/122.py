"""
# 单调优先队列
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        from collections import deque
        q = deque([prices[0]])
        size = len(prices)
        buy_flag = 0
        ans = 0
        for i in range(1, size):
            if not q:
                q.append(prices[i])
                continue
            if prices[i] > q[-1]:
                q.append(prices[i])
                buy_flag = 1
            else:
                if len(q) >= 2:
                    profit = q[-1] - q[0]
                    ans += profit
                    q = deque([prices[i]])
                else:
                    q.pop()
                    q.append(prices[i])
        if len(q) >= 2:
            profit = q[-1] - q[0]
            ans += profit
        return ans
prices = [1,2,3,4,5]
ans = Solution().maxProfit(prices)


