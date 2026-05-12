class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        freq = [[] for i in range(len(nums) +1)]
        
        for num in nums:
            bucket[num] = 1 + bucket.get(num, 0)
        for key, val in bucket.items():
            freq[val].append(key)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
