#Leet Code challenge

class Solution:
    def singleNumber(self, nums:[int]) -> int:
        # Get the first number
        result = nums[0]

        # Do XOR of all elements starting from index 1 and return the single repeating number,
        for i in range(1, len(nums)):
            # Do XOR
            result = result ^ nums[i]

        # Print result
        print(result)
        # Return result
        return result

# Main Call
solution =  Solution()
result = solution.singleNumber([1,1,2,2,3,4,4,5,5])
print(result)
