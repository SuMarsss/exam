"""
date： 2020年6月7日
starting time： 5.55pm 6.06pm
terminal time：6.43pm
"""
n = 7168


# def numSquares(n) :
#     import math
#     from collections import  deque
#     base = math.floor(n**0.5)
#     base_nums = [i**2 for i in range(base, 0 ,-1)]
#     q = deque()
#     q.append((n,1))
#
#     visited = set()
#     while q:
#         n, c = q.popleft()
#         if n in visited:
#             continue
#         else:
#             visited.add(n)
#         for i in base_nums:
#             if n > i :
#                 q.append((n-i, c+1))
#             elif n == i:
#                 return c

def numSquares(n):
    def is_divided_by(n, count):
        """
            return: true if "n" can be decomposed into "count" number of perfect square numbers.
            e.g. n=12, count=3:  true.
                 n=12, count=2:  false
        """
        if count == 1:
            return n in square_nums

        for k in square_nums:
            if is_divided_by(n - k, count - 1):
                return True
        return False

    square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

    for count in range(1, n + 1):
        if is_divided_by(n, count):
            return count



c = numSquares(11)


