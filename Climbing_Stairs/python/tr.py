#!/usr/bin/env python3


def haja(nums,target):
    nums = sorted(nums)

    for i in nums:
        if nums[i] == target:
            try:
                print(i)
            except:
                print("can't help you bro")




haja([1,3,5,6],5)
#output should be 2


haja([1,3,4,6],2)
# output should be 1


haja([1,3,5,6],7)
# output should be 4

