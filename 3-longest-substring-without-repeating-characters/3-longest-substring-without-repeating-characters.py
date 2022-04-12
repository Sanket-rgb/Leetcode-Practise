class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
#         substring = ""
#         longest_substring = ""
#         i = 0
        
#         for j in range(len(s)):
#             if s[j] not in s[i:j]:
#                 pass
#             else:
#                 substring = s[i:j]
#                 if len(substring) > len(longest_substring):
#                     longest_substring = substring
#                 i = j
        
#         if len(substring) == 0 or len(longest_substring) == 0:
#             return len(s)
#         else:
#             return len(longest_substring)

                