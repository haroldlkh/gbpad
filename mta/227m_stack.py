# class Solution(object):
#     def calculate(self, s):

#         operations = {
#             '+': lambda x, y: x + y,
#             '-': lambda x, y: x - y,
#             '*': lambda x, y: x * y,
#             '/': lambda x, y: x / y if y != 0 else 'Division by zero'
#         }
#         tmpnum=''
#         nums=[]
#         op_order=[]
#         for i,c in enumerate(s):
#             if c in operations:
#                 nums.append(int(tmpnum))
#                 op_order.append(c)
#                 tmpnum=''
#             else: tmpnum+=c
#             if i==len(s)-1: nums.append(int(tmpnum))

#         if len(op_order)==0: return nums[0]

#         correct_order=[]
#         for i,op in enumerate(op_order):
#             if op == '*' or op == '/':
#                 correct_order = [(i,op)] + correct_order
#             else: correct_order.append((i,op))

#         result = operations[correct_order[0][1]](nums[correct_order[0][0]], nums[correct_order[0][0]+1])
#         correct_order = correct_order[1:]
#         for op in correct_order:
#             result = operations[op[1]](result, nums[op[0]])
#         return result

class Solution:
    def calculate(self, s):
        operations = ['+', '-', '*', '/']
        stack = []
        num = 0
        prev_op = '+'

        # Iterate through the string
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)  # Build the current number
            if c in operations or i == len(s) - 1:  # End of number or operator
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack[-1] = stack[-1] * num
                elif prev_op == '/':
                    # stack[-1] = int(stack[-1] / num)
                    stack[-1] = int(stack[-1] / num) if stack[-1] >= 0 else -(-stack[-1] // num) #jank

                num = 0
                prev_op = c  # Update the previous operator

        return sum(stack)  # Final result is the sum of the stack
