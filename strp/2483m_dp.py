# class Solution:
#     def bestClosingTime(self, customers: str) -> int:
#         n = len(customers)
        
#         # Precompute prefix_N: number of 'N' up to each index
#         prefix_N = [0] * (n + 1)
#         for i in range(0, n):
#             prefix_N[i+1] = prefix_N[i] + (1 if customers[i] == 'N' else 0)
        
#         # Precompute suffix_Y: number of 'Y' from each index to the end
#         suffix_Y = [0] * (n + 1)
#         for i in range(n-1, -1, -1):
#             suffix_Y[i] = suffix_Y[i+1] + (1 if customers[i] == 'Y' else 0)
        
#         # Calculate the penalty for each closing hour
#         min_penalty = float('inf')
#         best_hour = 0
#         for i in range(n + 1):
#             penalty = prefix_N[i] + suffix_Y[i]
#             if penalty < min_penalty:
#                 min_penalty = penalty
#                 best_hour = i
        
#         return best_hour

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = score = 0
        best_hour = -1

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score, best_hour = score, i
                
        return best_hour + 1
