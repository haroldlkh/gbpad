class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec1 = {i:n for i,n in enumerate(nums) if n}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        if len(self.vec1) > len(vec.vec1):
            return vec.dotProduct(self)
        
        total = 0
        for i in self.vec1:
            if i in vec.vec1:
                total+= self.vec1[i] * vec.vec1[i]
            # total += self.vec1.get(i, 0) * vec.vec1.get(i, 0) #return 0 if get(i) is not possible
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
