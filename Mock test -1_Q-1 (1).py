def moveZeroes( nums):
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

nums= [0,1,0,3,12]
print(moveZeroes( nums))
