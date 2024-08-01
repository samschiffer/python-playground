class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        y = 0
        while x > 0:
            remainder = x % 10
            y = y * 10 + remainder
            x = x // 10
        y = y if not negative else -y
        return 0 if y > (2 ** 31 - 1) or y < (-2 ** 31) else y


if __name__ == "__main__":
    num = 1563847412
    print(2**31)
    print(num.bit_length())
    solution = Solution()
    print(solution.reverse(num))
