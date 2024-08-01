class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numLookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        index = 0
        while(index < len(s)):
            curNum = numLookup[s[index]]
            try:
                nextNum = numLookup[s[index + 1]]
            except:
                nextNum = -1

            if(curNum >= nextNum):
                sum += curNum
                index += 1
            else:
                sum += nextNum - curNum
                index += 2
        return sum

if __name__ == "__main__":
    print(Solution().romanToInt("LVIII"))
    # print(Solution().isPalindromeHelper(12)[0])
    # print(Solution.isPalindromeHelper(Solution, 102345))