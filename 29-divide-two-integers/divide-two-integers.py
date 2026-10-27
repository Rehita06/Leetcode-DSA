class Solution:
    def divide(self, dividend, divisor):
        a, b = abs(dividend), abs(divisor)
        result = 0

        while a >= b:
            temp, count = b, 1

            while a >= (temp << 1):
                temp <<= 1
                count <<= 1

            a -= temp
            result += count

        if (dividend < 0) != (divisor < 0):
            result = -result

        return min(max(result, -2**31), 2**31 - 1)