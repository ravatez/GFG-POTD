#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        negative=[x for x in arr if x<0]
        positive=[x for x in arr if x>=0]        
        result=[]
        i,j=0,0
        for k in range(len(arr)):
            if k%2==0 and i<len(positive):
                result.append(positive[i])
                i+=1
            elif j<len(negative):
                result.append(negative[j])
                j+=1
        result.extend(positive[i:])
        result.extend(negative[j:])
        for x in range(len(arr)):
            arr[x]=result[x]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends