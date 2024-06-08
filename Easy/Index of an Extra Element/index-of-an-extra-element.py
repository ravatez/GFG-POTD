class Solution:
    def findExtra(self,n,a,b):
        #add code here
        return a.index(list(set(a)-set(b))[0])

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends