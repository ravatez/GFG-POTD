#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        i=0
        l,r=0,0
        while i<k:
            
            if arr1[l]<=arr2[r]:
                i+=1
                l+=1
            elif arr1[l]>arr2[r]:
                i+=1
                r+=1
                
            if l==len(arr1):
                return arr2[k-len(arr1)-1]
                
            if r==len(arr2):
                return arr1[k-len(arr2)-1]
                
            
            if i==k-1:
                break
        
        return min(arr1[l],arr2[r])
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends