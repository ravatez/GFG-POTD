class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        n=len(arr)
        max1=1
        for i in range(len(arr)-1):
            sum1=arr[i]+arr[i+1]
            max1=max(sum1,max1)
        if max1==1:
            return -1
        return max1
    



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends