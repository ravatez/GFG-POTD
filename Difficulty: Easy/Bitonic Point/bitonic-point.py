#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
        low,high=0,len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]>arr[mid+1]:
                high=mid
            else:
                low=mid+1
        return arr[low]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends