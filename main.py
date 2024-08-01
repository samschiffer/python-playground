class Solution(object):
    def isPalindrome(self, x):
        result = False
        if x >= 0:
            # reverseNum, level = self.isPalindromeHelper(x)[0]
            result = (self.isPalindromeHelper(x)[0] == x)
        return result

    def isPalindromeHelper(self, number):
        last_digit = number % 10
        new_number = number // 10
        if new_number == 0:
            return last_digit, 1
        else:
            sumNumber, level = self.isPalindromeHelper(new_number)
            sumNumber += last_digit * 10 ** level
            return sumNumber, level + 1


if __name__ == "__main__":
    print(Solution().isPalindrome(12200221))
    # print(Solution().isPalindromeHelper(12)[0])
    # print(Solution.isPalindromeHelper(Solution, 102345))