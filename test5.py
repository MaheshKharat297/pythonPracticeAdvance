def count_match(str1, str2):
    count = 0
    match_lst = []
    for s in str1.lower():
        if s in str2.lower() and s not in match_lst:
            count = count + 1
            match_lst.append(s)
    print("Count of match is :", count)
    print("list of matching chars are :", match_lst)

str1 = 'abcdefdK'
str2 = 'abklpwowiwc'
count_match(str1, str2)


