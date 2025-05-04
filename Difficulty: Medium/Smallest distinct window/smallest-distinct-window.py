#User function Template for python3

class Solution:
    def findSubString(self, str):
        # code here
        i,j=0,0
        s=set(str)
        map = {}
        ans=len(str)
        while i<len(str):
            map[str[i]] = map.get(str[i],0)+1
            if len(map)==len(s):
                while (map[str[j]]>1):
                    map[str[j]]-=1
                    j+=1
                ans=min(ans,i-j+1)
            i+=1
        return ans    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends