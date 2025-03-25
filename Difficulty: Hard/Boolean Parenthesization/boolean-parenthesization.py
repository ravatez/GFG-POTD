#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        from functools import lru_cache
        @lru_cache(None)
        def dp(l=0,r=len(s)-1):
            nonlocal s
            if l==r:
                return (1,0,) if s[l]=='T' else (0,1,)
            t,f=0,0
            for m in range(l+1,r):
                op=s[m]
                if op not in '&|^':
                    continue
                l1,l2=dp(l,m-1)
                r1,r2=dp(m+1,r)
                if op=='&':
                    t+=l1*r1
                    f+=(l1+l2)*(r1+r2)-l1*r1
                elif op=='|':
                    t+=(l1+l2)*(r1+r2)-l2*r2
                    f+=l2*r2
                elif op=='^':
                    t+=l1*r2+l2*r1
                    f+=l1*r1+l2*r2
            return t,f
        return dp()[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends