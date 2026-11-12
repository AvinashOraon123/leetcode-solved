class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0]*n
        for i in range(k):
            new = [0]*n
            for curr in range(n):
                best = dp[curr] + stayScore[i][curr]
                for prev in range(n):
                    if prev!= curr:
                        v = dp[prev] + travelScore[prev][curr]
                        if v> best:
                            best = v
                new[curr] = best
            dp =new
        return max(dp)