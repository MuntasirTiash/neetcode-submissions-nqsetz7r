class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []

        for o in operations:
            if o == '+':
                nums.append(nums[-1] + nums[-2])
            elif o == 'C':
                nums.pop()
            elif o == 'D':
                nums.append(nums[-1] * 2)
            else:
                nums.append(int(o))

        return sum(nums)
