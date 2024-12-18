class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stackc = []
        stacki= []
        for i,c in enumerate(s):
            if c == '(':
                    stacki.append(i)
                    stackc.append(c)
            if c == ')':
                if len(stackc)==0:
                    stacki.append(i)
                    stackc.append(c)
                elif stackc[-1]=='(':
                    stackc.pop()
                    stacki.pop()
                else:
                    stacki.append(i)
                    stackc.append(c)

        add = 0
        for i in stacki:
            pos = i - add
            s = s[:pos] + s[pos+1:]
            add+=1
        
        return s


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # To track indices of unmatched '('
        to_remove = set()  # To track all indices to remove
        
        # First pass: Identify invalid parentheses
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)  # Store index of '('
            elif c == ')':
                if stack:
                    stack.pop()  # Match with the last unmatched '('
                else:
                    to_remove.add(i)  # No matching '(' for this ')'
        
        # Add remaining unmatched '(' indices to the removal set
        to_remove.update(stack)
        
        # Second pass: Build the result string
        result = ''
        for i, c in enumerate(s):
            if i not in to_remove:
                result+=c
        
        return result
