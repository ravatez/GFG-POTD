#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1] * n

        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= arr[i]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= arr[i]

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends