class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        l, r = 0, size-1
        maxRes = 0
        while l<=r:
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            maxRes = max((r-l+1) * h, maxRes)
        return maxRes
height = [1,8,6,2,5,4,8,3,7]
ans = Solution().maxArea(height)