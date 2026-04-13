class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        HashMap = {}
        for i in range(n):
            HashMap[students[i]] = HashMap.get(students[i],0) + 1

        for i in range(n):
            val = HashMap.get(sandwiches[i],0)

            if val > 0:
                HashMap[sandwiches[i]] = HashMap[sandwiches[i]] - 1
            else:
                break

        return sum(HashMap.values())