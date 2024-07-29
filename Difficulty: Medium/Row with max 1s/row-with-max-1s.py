#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
        max1=0
        store=-1
        for j in range(len(arr)):
            count=0
            for i in range(len(arr[j])):
                if arr[j][i]==1:
                    count+=1
                elif arr[j][i]==0:
                    count+=0
                else:
                    store=-1
                    
                    
            if max1<count:
                max1=count
                store= j
        return store

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends