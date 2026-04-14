class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i- nums[i])
        return res

        """ nums[i] = 3
            res = 3 + (0 - 3)
            res = 0
            
            res = (0 + 1 + 2 + 3) - (3 + 0 + 1)
            res = 6 - 4 = 2
            
            """