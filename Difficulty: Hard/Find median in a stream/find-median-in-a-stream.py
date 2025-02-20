
class Solution:
    def getMedian(self, arr):
        import heapq
        ret,up,dn=[],[],[]
        for ve in arr:
            ve=heapq.heappushpop(up,ve)
            ve=-heapq.heappushpop(dn,-ve)
            if len(up)==len(dn):
                ret.append(ve)
                heapq.heappush(up,ve)
            elif len(up)>len(dn):
                ret.append((up[0]+ve)/2)
                heapq.heappush(dn,-ve)
            else:
                ret.append((-dn[0]+ve)/2)
                heapq.heappush(up,ve)
        return ret

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends