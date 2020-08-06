# starting time: 2020年8月2日15:59:18
# terminal time:
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter,defaultdict
        cnt = Counter(tasks)
        lasts = defaultdict(int)

        def dfs( lasts, cnt, res):
            for (task, last) in lasts:
                if last == 0 and cnt[task]!= 0:
                    lasts_copy, cnt_copy = lasts.copy(), cnt.copy()
                    lasts_copy[task] = n
                    cnt_copy[task] -= 1
                    dfs(lasts_copy, cnt_copy, res+1)


        for task in cnt:
            lasts[task] = n
            cnt_ = cnt.copy()
            cnt_[task] -= 1
            res = 1
            dfs( lasts, cnt_,res)



tasks = ["A", "A", "A", "B", "B", "B"]
n = 2