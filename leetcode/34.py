class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        l,r = 0, size-1
        mid = (l+r)//2
        Flag = 0
        while l<=r:
            if nums[mid]<target:
                l = mid+1
            elif nums[mid] > target:
                r = mid -1
            else:
                Flag = 1
                break
            mid = (l+r)//2
        if Flag :
            st = mid
            while  st>=0 and nums[st ]== nums[mid] :
                if 0<st<=size-1:
                    st -= 1
                elif st <= 0:
                    st =-1
                    break
            st += 1

            end = mid
            while end<=size-1 and  nums[end] == nums[mid] :
                if end <size-1:
                    end += 1
                else:
                    end = size
            end -=1
            return (st, end)
        else:
            return (-1,-1)
nums = [1]
target = 1
ans = Solution().searchRange(nums, target)