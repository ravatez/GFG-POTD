#User function Template for python3
import heapq
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
          
        # making life simple (why to compare each and every elemet)
        iter=list(set(arr))
        if len(iter)<2:
            return -1
        x=heapq.nlargest(2,iter)
        return x[-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends