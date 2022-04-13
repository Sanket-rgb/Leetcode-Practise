class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        charSet = set()
        
        for i in range(len(nums)):
            if nums[i] in charSet:
                return True
            else:
                charSet.add(nums[i])
        return False
        