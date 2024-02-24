class Solution:
    #Time: O(N^2) Space: O(N)
    def findDisappearedNumbers1(self, nums):
        n = len(nums)
        missing = []
        for i in range(1, n+1):
            found = False
            for j in range(n):
                if i == nums[j]:
                    found = True
            if found == False:
                missing.append(i)
        return missing

    # Time: O(N) Space: O(N)
    def findDisappearedNumbers2(self, nums):
        n = set(nums)
        missing = []
        for i in range(1, n+1):
            if i not in nums:
                missing += [i]
        return missing
