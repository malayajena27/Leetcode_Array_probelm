class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = 0
        for i in range(n):
            if count == 0:
                ans = nums[i]
            if nums[i] == ans:
                count+=1
            else:
                count-=1
        return ans