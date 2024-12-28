class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s, left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        
        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return isValid(s, left+1, right) or isValid(s, left, right-1)
            left+=1
            right-=1
        return True
