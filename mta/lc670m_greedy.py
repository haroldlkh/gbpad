# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         numlist = []
#         while num>0:
#             numlist.append(num%10)
#             num//=10

#         numlist = numlist[::-1]
        
#         left=0
#         for i,n in enumerate(numlist):

#             sub_numlist = numlist[left:]
#             largest_digit_candidate = max(sub_numlist)
#             max_pos_candidate = sub_numlist.index(largest_digit_candidate)

#             if max_pos_candidate+left==left:
#                 left+=1
#             else:
#                 max_pos=max_pos_candidate+left
#                 largest_digit=largest_digit_candidate
#                 swap_pos = i

#         if left<len(numlist)-1:
#             numlist[max_pos] = numlist[left]
#             numlist[left] = largest_digit

#         for n in numlist:
#             num = num*10 + n

#        return num

class Solution:
    def maximumSwap(self, num: int) -> int:
        numlist = []
        while num>0:
            numlist.append(num%10)
            num//=10

        numlist = numlist[::-1]
        
        # Record the last occurrence of each digit
        last = {d: i for i, d in enumerate(numlist)}
        
        # Traverse the digits to find the first place to swap
        for i, d in enumerate(numlist):
            # Check if there is a larger digit to the right
            for larger in range(9, d, -1):  # Iterate over possible larger digits
                if larger in last and last[larger] > i:
                    # Swap the digits
                    numlist[i], numlist[last[larger]] = numlist[last[larger]], numlist[i]
                    # Return the result as an integer
                    for n in numlist:
                        num = num*10 + n
                    return num
        
        # If no swap is possible, return the original number
        for n in numlist:
            num = num*10 + n
        return num
