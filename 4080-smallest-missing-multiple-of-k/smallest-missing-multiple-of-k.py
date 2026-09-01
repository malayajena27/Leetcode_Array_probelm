
class Solution:

    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = []

        for i in range(len(nums)):
            if nums[i] % k == 0:
                l.append(nums[i])

        for i in range(1, len(nums) + 2):
            if i * k not in l:
                return i * k
