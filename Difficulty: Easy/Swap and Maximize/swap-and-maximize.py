#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        n = len(arr)
        s = 0
        for i in range(n):
            s += abs(arr[i]-arr[n-1-i])
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends