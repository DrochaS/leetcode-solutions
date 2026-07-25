class Solution:
    def getNSL(self , nums , n):
        st = []
        ans = []
        for i , val in enumerate(nums):
            if len(st) == 0:
                ans.append(-1)
            elif st and st[-1][0] < val:
                 ans.append(st[-1][1])
            elif st and st[-1][0] >= val:
                while st and st[-1][0] >= val:
                    st.pop()
                if len(st) == 0:
                    ans.append(-1)
                else:
                    ans.append(st[-1][1])
            
            st.append((val , i))
            
        return ans
    
    def getNSR(self , nums , n):
        st = []
        ans = []
        for i  in range(n - 1 , -1 , -1):
            val = nums[i]
            if len(st) == 0:
                ans.append(n)
            elif st and st[-1][0] < val:
                 ans.append(st[-1][1])
            elif st and st[-1][0] >= val:
                while st and st[-1][0] >= val:
                    st.pop()
                if len(st) == 0:
                    ans.append(n)
                else:
                    ans.append(st[-1][1])
            
            st.append((val , i))
            
        return list(reversed(ans))

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights) 
        left = self.getNSL(heights , n)
        right = self.getNSR(heights , n)

        width = [0] * n
        
        for i in range(n):
            width[i] = right[i] - left[i] - 1
        
        maxArea = float('-inf')
        for i in range(n):
            maxArea = max(maxArea , heights[i] * width[i])
        
        return maxArea