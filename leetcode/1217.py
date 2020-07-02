class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        size = len(chips)
        odd_cnt = 0
        even_cnt =0
        for i in range(size):
            if chips[i] % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return  min(even_cnt, odd_cnt)

chips = [2,2,2,3,3]
ans = Solution().minCostToMoveChips(chips)
