#解题
#1、循环
#2、哈希（字典）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums,start=1):
            if hashmap.get(target-num) is not None:
                return [i,hashmap.get(target-num)]
            hashmap[num]=i


