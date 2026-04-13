class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # max possible length

        # Multiply digit by digit (right to left)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                p1, p2 = i + j, i + j + 1  # positions in result array
                total = mul + result[p2]

                result[p2] = total % 10   # current digit
                result[p1] += total // 10  # carry

        # Build the final string, skipping leading zeros
        return "".join(str(d) for d in result).lstrip("0")