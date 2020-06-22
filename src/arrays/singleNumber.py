# Leet Code challenge

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        dict = {}

        for val in nums:
            if not val in dict:
                dict[val] = 1
            else:
                dict[val] += 1

        for k, v in dict.items():
            if v == 1:
                return k


# Main Call
solution = Solution()
result = solution.singleNumber([1, 1, 2, 2, 3, 4, 4, 5, 5])
print(result)
