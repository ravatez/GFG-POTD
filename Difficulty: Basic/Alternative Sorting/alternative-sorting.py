class Solution:
    def alternateSort(self,arr):
        # Your code goes here
               
        # Sort the array
        arr.sort()
        
        # Create a result list to store the alternative sorted elements
        result = []
        
        # Pointers to the beginning and end of the sorted array
        left, right = 0, len(arr) - 1
        
        # Alternate between the largest and smallest elements
        while left <= right:
            if left <= right:
                result.append(arr[right])
                right -= 1
            if left <= right:
                result.append(arr[left])
                left += 1
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends