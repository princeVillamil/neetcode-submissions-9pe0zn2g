class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i in range(len(nums)):
            if target - nums[i] in bucket:
                print(bucket,"-----", max(target, nums[i]) ,"-", min(target, nums[i]), "=", (max(target, nums[i]) - min(target, nums[i]))  )
                return [bucket[target - nums[i]], i]

            bucket[nums[i]] = i

        return []