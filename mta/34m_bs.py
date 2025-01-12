class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target, first=True):
            left = 0
            right = len(nums)-1
            bound=-1

            while left<=right:
                mid = (left+right)//2
                if nums[mid]==target:
                    bound=mid
                    if first: right = mid-1
                    else: left = mid+1

                elif nums[mid]>target: right = mid - 1
                else: left = mid + 1
            return bound

        start = bs(nums,target)
        end = bs(nums,target,False)

        return [start,end]


