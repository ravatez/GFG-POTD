#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        ans = 0
        for i in str(n):
            ans += (int(i)**3)
        if ans == n:
            return "true"
        return "false"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends