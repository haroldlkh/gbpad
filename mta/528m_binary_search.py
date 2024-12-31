# class Solution:

#     def __init__(self, w: List[int]):
#         self.wl = w

#         # self.weighted_lst = []
#         # for i,weight in enumerate(w):
#         #     self.weighted_lst += [i]*weight

#     def pickIndex(self) -> int:
#         return random.choices(range(0,len(self.wl)), self.wl, k=1)[0]
#         # return self.weighted_lst[random.randint(0,len(self.weighted_lst)-1)]

class Solution:

    def __init__(self, w: List[int]):
        # Create a prefix sum array for the weights
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # Generate a random number in the range [1, total_sum]
        target = random.randint(1, self.total_sum)
        
        # Perform a binary search to find the target's index in prefix_sums
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
