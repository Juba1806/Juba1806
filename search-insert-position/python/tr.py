#!/usr/bin/env python3


def haja(nums,target):
    nums = sorted(nums)

    for a,b in enumerate(nums):
        if target <= b:
            return print(a)

        return print(len(nums))



haja([1,3,5,6],5)
#output should be 2


haja([1,2,3,4],2)
# output should be 1



haja([1,3,4,6],2)
# output should be 1


haja([1,3,5,6],7)
# output should be 4

