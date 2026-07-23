class Solution:
    def searchInsert(self, nums: List[int], val: int) -> int:
        n = len(nums)

        for i in range(n):
            if val<=nums[i]:
                return i
        return n