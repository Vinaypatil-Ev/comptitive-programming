class SCS:
    def lcs(self, s1, s2, n, m):
        dp = [[""] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = ""
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[n][m]
    def scs(self, s1, s2, n, m):
        s = self.lcs(s1, s2, n, m)
        p1 = p2 = 0
        ans = ""
        for i in s:
            while s1[p1] != i:
                ans += s1[p1]
                p1 += 1
            while s2[p2] != i:
                ans += s2[p2]
                p2 += 1
            ans += i
            p1 += 1
            p2 += 1
        ans += s1[p1:] + s2[p2:]
        return ans


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    s = SCS()
    print(s.scs(s1, s2, len(s1), len(s2)))
