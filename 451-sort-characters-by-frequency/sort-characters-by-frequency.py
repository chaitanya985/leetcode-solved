class Solution:
    def frequencySort(self, s: str) -> str:

        counts=defaultdict(int)

        for char in s:

            counts[char]+= 1

            sorted_str = "".join(char * count for char, count in sorted(counts.items(), key=lambda x:(-x[1], x[0])))

        return sorted_str
        