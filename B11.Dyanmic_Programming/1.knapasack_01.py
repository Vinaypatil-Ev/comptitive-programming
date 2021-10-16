# recursive solution
def knapsack_01(wt, profit, size, n):
    if size == 0 or n == 0:
        return 0
    if wt[n] > size:
        return knapsack_01(wt, profit, size, n - 1)
    else:
        return max(
            knapsack_01(wt, profit, size, n - 1), 
            profit[n] + knapsack_01(wt, profit, size - wt[n], n - 1)
            )
        
# dp solution
d = dict()
def ks(wt, profit, size, n):
    if size == 0 or n == 0:
        return 0
    if (size, n) not in d:
        if wt[n] > size:
            d[(size, n)] = ks(wt, profit, size, n - 1)
        else:
            d[(size, n)] = max(
                ks(wt, profit, size, n - 1),
                profit[n] + ks(wt, profit, size - wt[n], n - 1)
            )
    return d[(size, n)]

# tabulization dp solution
def kst(wt, profit, size, n):
    dp = [[None] * (size + 1)] * (n + 1)
    for i in range(n + 1):
        for w in range(size + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], profit[i - 1] + dp[i - 1][w - wt[i - 1]])
    print(dp)
    return dp[n][size]
        

if __name__ == "__main__":
    wt = [3, 4, 1]
    profit = [5, 6, 2]
    size = 6
    x = knapsack_01(wt, profit, size, len(wt) - 1)
    print(f"max profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    wt = [3, 4, 2]
    profit = [5, 6, 4]
    size = 6
    x = knapsack_01(wt, profit, size, len(wt) - 1)
    print(f"max profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    profit = [60, 100, 120]
    wt = [10, 20, 30]
    size = 50
    x = knapsack_01(wt, profit, size, len(wt) - 1)
    print(f"max profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    x = ks(wt, profit, size, len(wt) - 1)
    print(f"\nwith dp \nmax profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    
    wt = [3, 4, 1]
    profit = [5, 6, 2]
    size = 6
    x = kst(wt, profit, size, len(wt))
    print(f"\nwith dp \nmax profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    
    profit = [60, 100, 120]
    wt = [10, 20, 30]
    size = 50
    x = knapsack_01(wt, profit, size, len(wt) - 1)
    print(f"max profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    x = ks(wt, profit, size, len(wt) - 1)
    print(f"\nwith dp \nmax profit for \nwt: {wt} and \nprofit: {profit} \nis: {x}")
    