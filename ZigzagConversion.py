class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        maxStep = (numRows - 1) * 2
        final_string = ""
        for curRow in range(numRows):
            step = maxStep - (2 * curRow)
            index = curRow
            while index < len(s):
                final_string += s[index]
                if step == 0:
                    step = maxStep
                index += step
                step = maxStep - step
        return final_string

if __name__ == "__main__":
    numRows = 5
    word = "PAYPALISHIRING"
    solution = Solution()
    print(solution.convert(word, numRows))
