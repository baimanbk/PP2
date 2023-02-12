#8th task
def spy_game(listik):
    for i in range(len(listik)):
        if i==len(listik)-1:
                return False
        if listik[i]==0:
            for x in range(i+1,len(listik)):
                if x==len(listik)-1:
                    return False
                if listik[x]==0:
                    for k in range(x+1,len(listik)):
                        if listik[k]==7:
                            return True
                        if k==len(listik)-1:
                            return False
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))