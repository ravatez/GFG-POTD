# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1]  # Initialize stack with base index
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        
        return max_len

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends