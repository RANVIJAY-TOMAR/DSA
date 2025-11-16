class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Clean the array of useless numbers.
        # We replace them with a positive value we can ignore: n + 1.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # 2. Mark the presence of numbers [1, n] by flipping signs.
        # We use the array's indices as our "hash set".
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                # Get the target index and ensure the value is positive before flipping.
                # A value might already be negative from a previous mark.
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        # 3. Find the first positive value. Its index reveals the missing number.
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all numbers [1, n] were present, the missing number is n + 1.
        return n + 1