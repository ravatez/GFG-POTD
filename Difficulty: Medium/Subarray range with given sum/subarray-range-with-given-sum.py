#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        # Initialize sum and count variables
        sum = 0  # To store the cumulative sum
        count = 0  # To store the count of subarrays that sum to the target
        mp = {}  # Dictionary to store the frequency of cumulative sums
    
        # Iterate through the array
        for i in range(len(arr)):
            sum += arr[i]  # Add the current element to the cumulative sum
    
            # If the cumulative sum equals the target, increment count
            if sum == tar:
                count += 1
    
            # If (sum - target) exists in the dictionary, it means there is
            # a subarray that sums to the target, so increment count by its frequency
            if (sum - tar) in mp:
                count += mp[sum - tar]
    
            # Store the current cumulative sum in the dictionary or update its frequency
            if sum in mp:
                mp[sum] += 1
            else:
                mp[sum] = 1
    
        return count  # Return the total count of subarrays that sum to the target

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends