class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    n = len(s)
    dp = [1] * n
    for j in range(1, n):
      pre = dp[j]
      for i in range(j-1, -1, -1):
        tmp = dp[i]
        if s[i] == s[j]:
          dp[i] = 2 + pre if i + 1 <= j - 1 else 2
        else:
          dp[i] = max(dp[i + 1], dp[i])
        pre = tmp
    return dp[0]