class Solution:
    def myAtoi(self, s):
        i = 0
        sign = 1
        num = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1

        num *= sign
        return max(-2**31, min(num, 2**31 - 1))