class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_s = set()
        longest = 0
        for i in range(len(s)):
            longest_s.clear()
            longest_s.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in longest_s:
                    longest_s.add(s[j])
                else:
                    break
            print(f"longest = {longest}")
            print(f"longest_s = {longest_s}")
            longest = max(longest, len(longest_s))
        return longest