class Solution:
    def sumSubstrings(self,s):
        # code here
        n=len(s)
        sum=0
        for i in range(n):
            for j in range(i+1,n+1):
                sum+=int(s[i:j])
        return sum