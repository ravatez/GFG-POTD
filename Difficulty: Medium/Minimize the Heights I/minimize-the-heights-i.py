#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        arr.sort() 
        n = len(arr)
        ans = arr[n-1] - arr[0] 
        for i in range(n) :
            mini = min(arr[0]+k , arr[i]-k) 
            maxi = max(arr[i-1]+k , arr[n-1]-k) 
            ans = min(ans , maxi - mini) 
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends