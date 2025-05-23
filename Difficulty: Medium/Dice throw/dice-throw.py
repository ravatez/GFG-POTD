class Solution:
    def binomial(self,n,k):
        if k<0 or k>n:
            return 0
        return math.comb(n,k)
    def noOfWays(self, m,n,x):
        # code here
        total=0
        max_k = (x-n)//m
        for k in range(max_k+1):
            term = (-1)**k * self.binomial(n,k) * self.binomial(x-m*k-1,n-1)
            total += term
        return total