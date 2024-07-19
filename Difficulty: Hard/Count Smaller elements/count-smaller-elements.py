#User function Template for python3
from sortedcontainers import SortedList
class Solution:

	def constructLowerArray(self,arr):
		# code here
        l = SortedList()
        output = [0] * len(arr)
        for i in reversed(range(len(arr))):
            l.add(arr[i])
            output[i] = l.index(arr[i])
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends