class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        last = len(heights)-1
        result=[last]
        tallest = heights[last]
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>tallest:
                result.append(i)
                tallest = heights[i]
        return result[::-1]
        
