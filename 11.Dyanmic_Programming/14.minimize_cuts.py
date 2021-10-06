class Solution:
    
    #Function to find the maximum number of cuts.
    def find(self, arr, size, N, d):
        dp = [[0] * (size + 1) for _ in range(N + 1)]
        for n in range(N + 1):
            for w in range(size + 1):
                if w == 0:
                    dp[n][w] = 0
                elif n == 0:
                    dp[n][w] = float("-inf")
                elif arr[n - 1] > w:
                    dp[n][w] = dp[n - 1][w]
                else:
                    dp[n][w] = max(1 + dp[n][w - arr[n -1]], dp[n - 1][w])
        return dp[n][w]
        
        # dp = [0] * (size + 1)
        # dp[0] = 1
        # for w in range(size + 1):
        #     for n in range(N):
        #         if arr[n] < w:
        #             dp[w] = max(1 + dp[w - arr[n]], dp[w])
                    
        # dp = [0] * (size + 1)
        # for n in range(N):
        #     for w in range(size + 1):
        #         if arr[n] <= w:
        #             dp[w] = max(1 + dp[w - arr[n]], dp[w])
        # return dp[size]
            
            
            
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        x = self.find([x, y, z], n, 3, {})
        return x if x > 0 else 0


if __name__ == "__main__":
    n = int(input())
    x, y, z = list(map(int, input().split()))
    s = Solution()
    x = s.maximizeTheCuts(n, x, y, z)
    print(x)