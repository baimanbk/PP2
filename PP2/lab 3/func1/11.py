def palindr(s = str(input())):
    s1 = s[::-1]
    if s1 == s:
        print('it is palindrome')
    else:
        print('it is not palindrome')
palindr()