class Solution:
    def isPalindrome(self, x: int) -> bool:
        n, r = 0, x
        while r > 0: n, r = n*10+r%10, r // 10
        return x == n