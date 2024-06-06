#User function Template for python3

def max_sum(a,n):
    #code here
    su=0
    prev=0
    
    for i in range(n):
        su+=a[i]
        prev+=(i*a[i])
    
    mi=prev
    for i in range(n):
        prev=( prev-(su-a[i]) )+ (a[i]*(n-1) )
        mi=max(mi,prev)
    return mi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends