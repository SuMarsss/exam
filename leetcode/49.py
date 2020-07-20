class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        d = defaultdict(list)
        for s  in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())

strs = ["eat","tea","tan","ate","nat","bat"]
ans = Solution().groupAnagrams(strs)
