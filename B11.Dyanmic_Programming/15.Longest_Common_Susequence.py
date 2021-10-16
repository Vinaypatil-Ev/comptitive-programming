class SQ:
    def __init__(self, s1, s2, n, m):
        # self.len = self.LCS_len(string1, string2)
        self.s1 = s1
        self.s2 = s2
        self.n = n
        self.m = m
    def LCS_rec(self):
        s1, s2, n, m = self.s1, self.s2, self.n, self.m
        def rec(s1, s2, n, m):
            if n == 0 or m == 0:
                return 0
            elif s1[n - 1] == s2[m - 1]:
                return 1 + rec(s1, s2, n - 1, m - 1)
            else:
                return max(rec(s1, s2, n - 1, m), rec(s1, s2, n, m - 1))
        return rec(s1, s2, n, m)
        
    def LCS_itr(self, path=False):
        s1, s2, n, m = self.s1, self.s2, self.n, self.m
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        if path:
            return dp
        return dp[n][m]

    
    def LCS_rec_td(self, d={}):
        s1, s2, n, m = self.s1, self.s2, self.n, self.m
        d={}
        def rec(n, m):
            if n == 0 or m == 0:
                return 0
            if (n, m) not in d:
                if s1[n - 1] == s2[m - 1]:
                    d[(n, m)] = 1 + rec(n - 1, m - 1)
                else:
                    d[((n, m))] = max(rec(n - 1, m), rec(n, m - 1))
            return d[(n, m)]
        return rec(n, m)
    
    def find_path(self):
        s1, s2, n, m = self.s1, self.s2, self.n, self.m
        dp = self.LCS_itr(True)
        def itr(n, m, path=""):
            # i = dp[n][m]
            # path = [""] * i
            while n > 0 and m > 0:
                if s1[n - 1] == s2[m - 1]:
                    # path[i - 1] = s1[n - 1]
                    path = s1[n - 1] + " " + path
                    n -= 1
                    m -= 1
                    # i -= 1
                elif dp[n - 1][m] > dp[n][m - 1]:
                    n -= 1
                else:
                    m -= 1
            return path
        
    
        def rec(n, m, path=[]):
            if n == 0 or m == 0:
                return path
            if s1[n - 1] == s2[m - 1]:
                path.append(s1[n - 1])
                return rec(n - 1, m - 1)
            elif dp[n - 1][m] > dp[n][m - 1]:
                return rec(n - 1, m, path)
            else: 
                return rec(n, m - 1, path) 
            
        # return rec(n, m)
        return itr(n, m)
    def LCS_opt_space(self,):
        s1, s2, N, M = self.s1, self.s2, self.n, self.m
        X = [0] * (M + 1)
        Y = [0] * (M + 1)
        for n in range(N + 1):
            for m in range(M + 1):
                if n == 0 or m == 0:
                    X[m] = 0
                elif s1[n - 1] == s2[m - 1]:
                    X[m] = 1 + Y[m - 1]
                else:
                    X[m] = max(Y[m], X[m - 1])
            Y = X[:]
        # print(X)
        return X[M]
    
    def LCS_path(self):
        s1, s2, n, m = self.s1, self.s2, self.n, self.m
        dp = [[""] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = ""
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1] + " "
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]   
        return dp[n][m] 
                    
                

    
            


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    n = len(s1)
    m = len(s2)
    s = SQ(s1, s2, n, m)
    print(s.LCS_itr())
    # print(s.LCS_rec())
    # print(s.LCS_rec_td())
    print(s.LCS_opt_space())
    # print(s.find_path())
    print(s.LCS_path())