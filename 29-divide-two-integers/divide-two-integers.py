class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Special overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            quotient = quotient + multiple

        if negative:
            return -quotient

        return quotient