"""You are given an integer array digits, 
where each digits[i] is the ith digit of a large integer. 
It is ordered from most significant to least significant digit, 
and it will not contain any leading zero."""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]