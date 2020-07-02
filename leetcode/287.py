class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for num in nums:
            if num in visited:
                return num
            else:
                visited.add(num)