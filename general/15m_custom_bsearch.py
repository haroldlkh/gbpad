def count_triplets(nums, k):
    nums.sort()
    count = 0
    n = len(nums)

    for i in range(n-2):
        for j in range(i+1,n-1):
            complement = k - nums[i] - nums[j]
            left = j+1
            right = n-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] == complement:
                    count+=1
                    break
                elif nums[mid] > complement: right = mid-1
                else: left = mid+1
    return count

# sort: n log n
# bsearch: n
# loop each val over bsearch: n^2
# space: extra space: O(1), sort uses o(n)
