"""
LeetCode Challenge

Given an array of strings, group anagrams together.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # First Solution
        dic = {}
        for words in strs:
            sorted_word = "".join(sorted(words))
            if sorted_word not in dic:
                dic[sorted_word] = [words]
            else:
                dic[sorted_word].append(words)

        return dic.values()
        # Second Solution
        """
        output = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in output:
                output[x].append(i)
            else:
                output[x] = [i]
        return sorted(list(output.values()))
        """


# Main Call
solution = Solution()
result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
for items in result:
    print(items)
