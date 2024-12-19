# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # new = []
        # for i,n in enumerate(nums):
        #     if i == 0: new.append(n)
        #     if i>0:
        #         if n<new[len(new)]: new.append(n)

        # return new
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
