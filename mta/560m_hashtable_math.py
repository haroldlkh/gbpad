class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefsum = 0
        found = {0:1}
        for n in nums:
            prefsum+=n
            if prefsum-k in found:
                total+=found[prefsum-k]
            if prefsum not in found: found[prefsum] = 1
            else: found[prefsum]+=1
        return total
