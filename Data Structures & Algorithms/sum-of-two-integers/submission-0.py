class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF       # 32 ones: keeps only the lowest 32 bits
        max_int = 0x7FFFFFFF    # largest positive 32-bit number (31 ones)

        while b != 0:
            carry = ((a & b) << 1) & mask    # carries, trimmed to 32 bits
            a = (a ^ b) & mask               # sum without carry, trimmed to 32 bits
            b = carry

        # If the top bit is set, the 32-bit pattern represents a negative number
        return a if a <= max_int else ~(a ^ mask)