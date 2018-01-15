class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if temp < count:
                    temp = count
                count = 0
        if temp > count:
            return temp
        else:
            return coun