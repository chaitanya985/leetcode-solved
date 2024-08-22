class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count, prefix_sum, mod_count=0, 0, defaultdict(int)

        mod_count[0]=1

        for num in nums:

            prefix_sum+=num

            count+=mod_count[prefix_sum % k]

            mod_count[prefix_sum % k]+=1

        return count


        