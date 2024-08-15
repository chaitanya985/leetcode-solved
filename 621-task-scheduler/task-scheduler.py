class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_counts=Counter(tasks)

        max_counts = max(task_counts.values())

        max_task_counts = sum(1 for count in task_counts.values() if count==max_counts)

        intervals = (max_counts - 1) * (n + 1) + max_task_counts

        return max(intervals, len(tasks))


        