# import re
# class Solution:
#     def simplifyPath(self, path: str) -> str:
        
#         def is_valid(c):
#             return c not in {"/", ".", ".."}

#         sim = '/'
#         path=path[1:]
#         startdir = 0
#         temp_dir=''
#         dots=''
        
#         for i,c in enumerate(path):
#             if c == '/' and path[i-1] != '/':
#                 sim+=temp_dir+c
#                 temp_dir=''
#                 startdir = i+1
#             if is_valid(c): temp_dir+=c
#             if c == '.': dots+=c

#         return sim[:-1]

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for component in components:
            if component == '' or component == '.':
                # Ignore empty components and "."
                continue
            elif component == '..':
                # Navigate to the parent directory, if possible
                if stack:
                    stack.pop()
            else:
                # Push valid directory names onto the stack
                stack.append(component)
        
        # Rebuild the simplified path
        return '/' + '/'.join(stack)
