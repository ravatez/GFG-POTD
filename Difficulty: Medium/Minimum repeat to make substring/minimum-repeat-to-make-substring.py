#User function Template for python3

class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        n1 = len(s1)
        n2 = len(s2)
        k = (n2 // n1) + n1
        s = s1
        count = 1
        i = 0
        while i < k:
            if s.find(s2) != -1:
                return count
            else:
                count += 1
                s += s1
            i += 1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends