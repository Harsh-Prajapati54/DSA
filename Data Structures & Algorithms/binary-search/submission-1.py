class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            # find mid point inarray
            mid  = low + ( high - low ) // 2
            # if mid point is match return number 
            if nums[mid] == target:
                return mid
            # if not matched or greater than mid move right 
            elif nums[mid] <= target:
                low = mid + 1
            # if less than mid move left 
            else:
                high = mid - 1
        # if not found
        return -1

            