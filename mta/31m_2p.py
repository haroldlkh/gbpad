class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1: return

        pivot = n-2
        while pivot>=0 and nums[pivot]>=nums[pivot+1]: pivot-=1
        if pivot>=0:
            successor = n - 1
            while nums[successor] <= nums[pivot]: successor -= 1
            nums[pivot], nums[successor] = nums[successor], nums[pivot]
        
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
