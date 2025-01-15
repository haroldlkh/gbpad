class Solution:
    def customSortString(self, order: str, s: str) -> str:
        second = []
        order_dict = {c:0 for c in order}
        for c in s:
            if c not in order_dict: second.append(c)
            else: order_dict[c]+=1

        first = []
        for key,value in order_dict.items():
            first.append(key*value)

        return ''.join(first) + ''.join(second)

# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         # Count the frequency of characters in `s`
#         char_count = {}
#         for c in s:
#             char_count[c] = char_count.get(c, 0) + 1
        
#         # Build the result using the order in `order`
#         result = []
#         for c in order:
#             if c in char_count:
#                 result.append(c * char_count[c])
#                 del char_count[c]  # Remove the character from the count
        
#         # Add the remaining characters from `s` that are not in `order`
#         for c, count in char_count.items():
#             result.append(c * count)
        
#         return ''.join(result)
