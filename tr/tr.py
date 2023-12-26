#!/usr/bin/env python3




def removeDuplicates(nums):
    for i in range(len(nums)):
        if i < len(nums) -1 :
            if nums[i] == nums[i + 1]:
                nums.pop(nums[i])
                k = nums[i]
                k = "_"
                nums.append(k)
    print(nums)





removeDuplicates([1,2,2,3,4])
removeDuplicates([1,2,3,4,4,5])
removeDuplicates([1,2,3,4,5,5,6,7,8,9])
