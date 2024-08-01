class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring_len = 0
        longest_palindrome = ''
        for left_index in range(len(s)):
            for right_index in range(len(s) - 1, left_index - 1, -1):
                if (right_index - left_index) + 1 > max_substring_len:
                    if self.isPalindrome(s, left_index, right_index):
                        longest_palindrome = s[left_index:right_index + 1]
                        max_substring_len = right_index - left_index + 1
        return longest_palindrome

    @staticmethod
    def isPalindrome(s: str, start_index: int, end_index: int):
        while start_index <= end_index:
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True


if __name__ == '__main__':
    for i in range(1):
        print(i)
    solution = Solution()
    s = 'a'
    print(solution.longestPalindrome(s))
