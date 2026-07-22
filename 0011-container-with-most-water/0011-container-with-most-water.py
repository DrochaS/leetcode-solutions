class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n-1
        max_area = 0

        while l<r:
            distance = r - l
            mini = min(height[l],height[r])
            area = distance*mini

            if area>max_area:
                max_area = area
            
            if height[r]<height[l]:
                r-=1
            else:
                l+=1
        return max_area