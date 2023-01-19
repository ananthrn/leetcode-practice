class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        
        freqs = sorted(cnt.values())
        
        f_max = freqs.pop()
        
        idle_time = (f_max - 1) * n
        
        while freqs:
            f_next = freqs.pop()
            
            idle_time -= min(f_max - 1, f_next)
        
        return len(tasks) + max(0, idle_time)
        
        