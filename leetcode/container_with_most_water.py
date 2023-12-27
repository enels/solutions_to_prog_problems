class Solution:
    def maxArea(self, height: List[int]) -> int:

        # get the bar with the maximum height
        max_height = max(height)

        # find the index location of the first occurrence
        # of the bar with the maximum height
        height_length = len(height)
        for index in range(height_length):
            if height[index] == max_height:
                max_height_index = index
                break
        
        # get the largest area of the water
        # assuming largest area to be zero(0)
        max_area = 0
        
        # iterate through the bar lengths indexex
        # starting from the first occurence of the maximum bar index
        area = 0
        for index in range(height_length):
            count = 0
            # iterate through the bars
            # starting from the current bar
            if index != height_length - 1:

                for i in range(index+1, height_length):
                    count += 1
                    if height[i] <= height[index]:
                        area = height[i] * count

            # compare the area with the maximum area
            if area > max_area:
                max_area = area
        
        return max_area
