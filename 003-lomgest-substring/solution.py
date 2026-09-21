class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = ""
        longest = 0

        for ch in s:
            if ch in chars:
                chars = chars[chars.index(ch) + 1:]

            chars += ch
            longest = max(longest, len(chars))

        return longest