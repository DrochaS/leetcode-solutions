class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number and its index
        num_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # If complement exists in dictionary, return both indices
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store current number and its index
            num_to_index[num] = i
        
        # Should never reach here (problem guarantees one solution)
        return []