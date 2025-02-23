# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        # code here
        s=[]
        n=len(arr)
        res=[0 for i in range(n)]
        for i in range(n):
            if len(s)==0:
                s.append(i)
                continue
            while len(s)!=0 and arr[s[-1]]<arr[i] and i>0 :
                k=s.pop()
                res[k]=arr[i]
            s.append(i)
        for i in range(len(res)):
            if res[i]==0:
                res[i]=-1
        return res

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends