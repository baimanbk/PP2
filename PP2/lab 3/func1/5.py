import itertools
def permutation(s = str(input())):
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    print([''.join(permutation) for permutation in permutations])
permutation()
# itertools has 4 main function for sorting out
# 1 product
# 2 permutations
# 3 combinations
# 4 combinations_with_replacement