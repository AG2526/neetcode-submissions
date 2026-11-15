class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:               # while n is not 0
            n &= n - 1         # remove the lowest 1-bit
            count += 1         # one more 1 found

        return count