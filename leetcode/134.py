class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        nums = len(gas)

        st_i = []
        for i in range(nums):
            if gas[i] >= cost[i]: st_i.append(i)

        for j in st_i:
            state1 = 0
            i = j
            state2 = gas[i] - cost[i] + state1
            pos_set=set()
            Flag = 1
            while 1:
                if state2 >= 0:
                    pos_set.add(i)
                    nxt_i = i + 1 if i < nums -1 else 0
                    state1 = state2
                    state2 = state1 + gas[nxt_i] - cost[nxt_i]

                    i = nxt_i
                    if i == j: return j
                else:
                    Flag = 0
                    break
            if Flag == 1: return j
        return -1

gas  = [5]
cost = [5]
ans = Solution().canCompleteCircuit(gas,cost)


