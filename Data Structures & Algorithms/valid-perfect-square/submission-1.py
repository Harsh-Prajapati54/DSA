import math 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int(math.sqrt(num))
        return sqRoot * sqRoot == num

        