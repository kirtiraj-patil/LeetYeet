class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m - 1 == 0 or n - 1 == 0:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
