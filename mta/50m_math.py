class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0: return 0
            if n==0: return 1

            ans = power(x,n//2)
            ans*=ans
            if n%2==1:
                return ans*x
            return ans

        result = power(x,abs(n))
        if n>=0: return result
        return 1/result

if n is even
  x^n = x^(n/2) * x^(n/2)
n is odd
  x^n = x^((n-1)/2) * x^((n-1)/2) * n
