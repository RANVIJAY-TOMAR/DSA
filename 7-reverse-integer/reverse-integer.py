class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1   # 32-bit range

        sign = -1 if x < 0 else 1              # Store the sign
        x = abs(x)                             # Make x positive
        rev = 0                                # Reversed number starts as 0

        while x != 0:                          # Repeat until x is 0
            pop = x % 10                       # Get last digit
            x //= 10                           # Remove last digit
            rev = rev * 10 + pop               # Add digit to reversed number

        rev *= sign                            # Restore sign

        if rev < INT_MIN or rev > INT_MAX:     # Overflow check
            return 0

        return rev                             # Final reversed number
