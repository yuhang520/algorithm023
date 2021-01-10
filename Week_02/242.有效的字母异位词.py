#writed by 2020.01.10
#有效的字母异位词词：https://leetcode-cn.com/problems/valid-anagram/description/
#审题：
#1、由题目可知，是由相同字母构成的
#2、长度也一样
#解题：
#1、使用排序，排完之后再看是不是一样的 时间复杂度O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         str1=sorted(s,key=str.lower)
#         str2=sorted(t,key=str.lower)
#         if str1==str2:
#             return True
#         else:
#             return False
#2、计数，map，出现的次数一致就是一样
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        # map={}
        #map1={}
        # count=0
        # for i in s:
        #     if map.get(i):
        #
        #         map[i]+=1
        #     else:
        #         map[i]=1
        # for j in t:
        #     if map.get(j):
        #         map[j]+=1
        #     else:
        #         map[j]=1
        #  for x in map:
        #      if x not in map1 or map[x]!=map1[x]:
        #          return False
        #  return True
#3、哈希
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t)
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True
