class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hm:
                return [hm[complement] + 1, i + 1]  # 1-based indexing
            hm[num] = i
        return [-1, -1]