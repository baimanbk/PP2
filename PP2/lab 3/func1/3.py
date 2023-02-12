#3rd task
"""
    3rd task
    r=rabits c=chicken
                           4r + 2c = numheads
    1*r+1*c=numlegs  == || 4r + 4c = 4numlegs
                           2c=4numlegs-2numheads 
                           r = numheads-c
"""
def solve(numheads,numlegs):
    c = (numlegs - 2*numheads) /2 
    r = numheads - c
    r=int(r)
    c=int(c)
    return r,",", c

# print(*solve(35,94))