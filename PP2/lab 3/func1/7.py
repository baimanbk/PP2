#7th task

def has_33(*nums):
    d=0
    k=1
    while nums and d!=len(nums) and k!=len(nums)+1:
        if nums[d]==3 and nums[k]==3:
            return True
        d=d+1
        k=k+1
    return False

# print(has_33(2, 3, 3, 4, 5))

