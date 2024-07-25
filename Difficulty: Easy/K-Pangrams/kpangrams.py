#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
        curr = 26
        string = string.replace(' ', '')
        n = len(string)
        if n < 26:
            return False
        alphabet = [1] * 128
        for i in range(n):
            if string[i] == ' ':
                continue
            if alphabet[ord(string[i])] == 1:
                curr-=1
                alphabet[ord(string[i])]-=1
                if curr <= k:
                    return True
        
        if curr <= 0:
            return True
        else:
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends