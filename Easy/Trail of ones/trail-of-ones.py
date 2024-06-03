#User function Template for python3
class Solution:
    MOD = int(1e9 + 7)

    def power(self, a, b):
        ans = 1
        while b > 0:
            if b & 1:
                ans = (ans * a) % self.MOD
            a = (a * a) % self.MOD
            b >>= 1
        return ans

    def numberOfConsecutiveOnes(self, n: int) -> int:
        # Initialize the arrays a and b
        a = [0] * n
        b = [0] * n
        
        # Base cases
        a[0] = 1
        b[0] = 1
        
        # Fill the arrays using the recurrence relations
        for i in range(1, n):
            a[i] = (a[i-1] + b[i-1]) % self.MOD
            b[i] = a[i-1] % self.MOD
        
        # Total binary strings without consecutive ones
        total_without_consecutive_ones = (a[n-1] + b[n-1]) % self.MOD
        
        # Total binary strings of length n
        total_binary_strings = self.power(2, n)
        
        # Number of binary strings with consecutive ones
        result = (total_binary_strings - total_without_consecutive_ones + self.MOD) % self.MOD
        
        return result

       

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends