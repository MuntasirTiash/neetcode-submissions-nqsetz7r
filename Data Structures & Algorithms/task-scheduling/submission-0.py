class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_freq = max(counts.values())
        max_freq_tasks = list(counts.values()).count(max_freq)
        
        # Formula: (max_freq - 1) * (n + 1) + number of tasks with max frequency
        ans = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        # The answer cannot be smaller than the total number of tasks
        return max(ans, len(tasks))