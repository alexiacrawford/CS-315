import sys 
def max_coins(T, denominations):
    """
    Compute maximum number of coins that sums to T, given that 
    each denomination can be used at most 5 times
    """
    dp = [-1] * (T + 1)
    dp[0] = 0  #base case: 0 coins = sum 0

    for d in denominations:  #each denomination separately
            for i in range(5):  #use each denomination up to 5 times
                for v in range(T, d - 1, -1):  #Traverse backwards
                    if dp[v - d] != -1:  # If (v - d), update dp[v]
                        dp[v] = max(dp[v], dp[v - d] + 1)

    if dp[T] != -1:
        return dp[T]
    else:
        return -1

def main():
    """
    Reads input from a file and calls max_target_coins().
    """
    data = sys.stdin.read().splitlines()

    T, n = map(int, data[0].split())
    denominations = list(map(int, data[1].split()))

    print(max_coins(T, denominations))

if __name__ == "__main__":
    main()