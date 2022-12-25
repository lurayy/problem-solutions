# https://leetcode.com/problems/two-sum/


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, value in enumerate(nums):
            another = target - value
            if another in nums:
                another_index = nums.index(another)
                print(another_index, another)
                if another_index != index:
                    return [index, another_index]


cases = (([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]),
         ([3, 3], 6, [0, 1]), ([0, 4, 3, 0], 0, [0, 3]))

sols = Solution()
for index, case in enumerate(cases):
    if sols.twoSum(case[0], case[1]) == case[2]:
        print(f'Case {index} Passed')
        pass
    else:
        pass
        print(f'Case {index} failed')