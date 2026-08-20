class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums) 
        maximumsum = float("-inf")
        s = 0
        for i in range(n):
            s = s+ nums[i]
            maximumsum = max(s , maximumsum)
            if s <= 0:
                s = 0
        return maximumsum
