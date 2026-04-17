class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Find 2 indices: i1, i2 where: 
        # (i2 - i1) * min(heights[i1], heights[i2]) get the maximum value
        # Time complexity: O(n)
        # Space complexity: O(1)
        max_container_water = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                current_container_water = (j - i) * min(heights[i], heights[j])
                if  current_container_water > max_container_water:
                    max_container_water = current_container_water
        return max_container_water

        