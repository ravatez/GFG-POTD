#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        if n == 0 or n == 1:
            return 1

        a, b = 1, 1
        mod = 1000000007
        c = 0

        for i in range(n - 2):
            c = (a + b) % mod
            a = b % mod
            b = c % mod

        return c % mod

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends