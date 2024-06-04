#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
        n = int(s, 2)
    
        # Increment the integer by 1
        n += 1
        
        # Convert the incremented integer back to a binary string
        result = bin(n)[2:]
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends