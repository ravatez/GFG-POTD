#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
                # code here
        n=len(arr)
        m=n//2
        
        for k in range(1, m+1):
            # Right-rotate the array by 1 (clockwise)
            arr=[arr[-1]]+arr[:-1]
           
            # Delete the (n - k + 1)th element from the beginning 
            del_index=len(arr)-k
            arr.pop(del_index)
        
        return arr[0]


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends