class Missing_number:
    #Time: O(N^2) Space: O(1)
    def findDisappearedNumbers1(self, nums):
        n = len(nums)
        missing = []
        for i in range(1, n+1):
            found = False
            for j in range(n):
                if i == nums[j]:
                    found = True
                    break
            if found == False:
                missing.append(i)
        return missing

    # Time: O(N) Space: O(N)
    def findDisappearedNumbers2(self, nums):
        n = set(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if i not in n:
                missing += [i]
        return missing
    
    # Time: O(N) Space: O(1)
    #Explained in class
    def findDisappearedNumbers3(self, nums):
        missing = []

        #for every number num in nums, revert the sign for number at index num.
        #if the sign is not reverted, the number corresponding to it is missing.
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        #if the number at i is positive, the number i+1 is missing
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)
        return missing

