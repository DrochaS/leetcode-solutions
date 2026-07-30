class Solution:
    def rec(self, nums, i, curr, result):
        result.append(curr[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            curr.append(nums[j])
            self.rec(nums, j + 1, curr, result)
            curr.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.rec(nums, 0, [], result)
        return result