#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n = len(arr)
        max_so_far = arr[0]
        min_so_far = arr[0]
        res = arr[0]

        for i in range(1, n):
            if arr[i] < 0:
                max_so_far, min_so_far = min_so_far, max_so_far

            max_so_far = max(arr[i], max_so_far * arr[i])
            min_so_far = min(arr[i], min_so_far * arr[i])

            res = max(res, max_so_far)

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends