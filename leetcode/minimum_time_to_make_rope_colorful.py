class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        # get length of colors
        colors_len = len(colors)

        # total time to pick the colors
        total_time = 0

        for n in range(colors_len - 1):
            if colors[n] == colors[n+1]:
                # if comparing the last color
                if n+1 == colors_len-1:
                    total_time += neededTime[n+1]
                else:
                    total_time += neededTime[n]

        
        return total_tim
