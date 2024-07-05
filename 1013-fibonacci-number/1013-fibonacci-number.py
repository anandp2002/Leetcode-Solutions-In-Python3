class Solution:
    def fib(self, n: int) -> int:
        n1,n2=0,1
        if n==0:
            return 0
        elif n==1:
            return 1
        res=[n1,n2]
        for i in range(n-2):
            res.append(n1+n2)
            n1=n2
            n2=res[-1]
        return res[-1]+res[-2]