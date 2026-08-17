class Solution:
    def spiralOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums[0])
        n = len(nums)
        l=[]
        top,left,bottom,right = 0,0,n-1,m-1

        while top <= bottom and left <= right:

            for i in range(left,right+1):
                l.append(nums[top][i])
            top+=1

            for i in range(top,bottom+1):
                l.append(nums[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    l.append(nums[bottom][i])
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    l.append(nums[i][left])
                left+=1

        return l 