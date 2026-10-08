class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF

        max_int = 0x7FFFFFFF

        while b != 0:

            # Find the carry

            carry = (a & b) << 1

            # Add without carry

            a = (a ^ b) & mask

            # Move carry to the next iteration

            b = carry & mask

        # Convert negative results to signed integers

        if a > max_int:

            return ~(a ^ mask)

        return a