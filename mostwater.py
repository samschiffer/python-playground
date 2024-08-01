import math
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0
#         for i in range(len(height)):
#             minDistance = math.ceil(maxArea / height[i]) # the minimum distance away the other height needs to be
#             # look left
#             if i - minDistance >= 0:
#                 for leftIndex in range(i - minDistance, i):
#                     area = min(height[i], height[leftIndex]) * (i - leftIndex)
#                     if area > maxArea:
#                         maxArea = area
#                 minDistance = math.ceil(maxArea / height[i])
#             # look right
#             if i + minDistance < len(height):
#                 for rightIndex in range(i + minDistance, len(height)):
#                     area = min(height[i], height[rightIndex]) * (rightIndex - i)
#                     if area > maxArea:
#                         maxArea = area
#         return maxArea

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        leftIndex = 0
        rightIndex = len(height) - 1
        while (rightIndex > leftIndex):
            area = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex)
            if area > maxArea:
                maxArea = area
            if height[leftIndex] < height[rightIndex]:
                leftIndex += 1
            else:
                rightIndex -= 1
        return maxArea

if __name__ == "__main__":
    height = [2,4,9,7,3,5,6,6,4,2,1,8]
    solution = Solution()
    print(solution.maxArea(height))
