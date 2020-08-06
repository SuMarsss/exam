class Solution(object):
    def primePalindrome(self, N):
        def is_prime(n):
            return n > 1 and all(n % d for d in xrange(2, int(n**.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10**7 < N < 10**8:
                N = 10**8

