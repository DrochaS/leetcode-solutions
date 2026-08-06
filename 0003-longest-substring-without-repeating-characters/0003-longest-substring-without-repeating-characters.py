class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = p2 = 0
        seen = set()
        max_len = 0
        length = 0

        while p2 < len(s):
            if s[p2] in seen:
                for i in range(p1, p2):
                    if s[i] != s[p2]:
                        seen.remove(s[i])
                    else:
                        seen.remove(s[i])
                        p1 = i + 1
                        break
                length = p2 - i - 1             
            else:
                seen.add(s[p2])
                p2 += 1
                length += 1
            if length > max_len:
                max_len = length
        return max_len