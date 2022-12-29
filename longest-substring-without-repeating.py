# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        last = ''
        longest = 0
        for alpha in s:
            if alpha in last:
                last = last[last.index(alpha):]
            else:
                longest += 1
                last = f'{last}{alpha}'
        return longest


s = Solution()

print(s.lengthOfLongestSubstring('aabaab!bb'))
