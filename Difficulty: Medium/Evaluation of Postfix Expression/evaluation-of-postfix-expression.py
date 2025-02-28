#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        # code here
        # code here
        s = []
        for i in arr:
            if i in "+-*/":
                b, a = s.pop(), s.pop()
                if i == "+": s.append(a + b)
                elif i == "-": s.append(a - b)
                elif i == "*": s.append(a * b)
                else: s.append(int(a / b))
            else:
                s.append(int(i))
        return s[0]

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends