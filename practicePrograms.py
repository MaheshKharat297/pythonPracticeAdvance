#Module: collection of functions / methods, global variables in.py file
#Package: collection of modules i.e.py files and having __init__.py file
#library: collection of packages e.g pandas, Numpy
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

### to check prime numbers in given range of numbers
def prime_check(x, y):
    prim_lst = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
                else:
                    prim_lst.append(i)
    return prim_lst


start = 2
end = 7
prim_lst = prime_check(start, end)
if len(prim_lst) == 0:
    print(f"No prime number in range {start} to {end}")
else:
    print(f"Prime numbers in range {start} to {end} are :", prim_lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Prime number finding in given number range
def prim(num):
    prim_lst = []
    for i in range(num):
        count = 0
        for j in range(2, int((i / 2) + 1)):
            if i % j == 0:
                count = count + 1
                break
        if count == 0 and i not in prim_lst:
            prim_lst.append(i)

    print(prim_lst)


num = 10
prim(num)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###To check given number if fibonacci
def fib_check(num):
    seq = [0, 1]
    for i in range(len(seq), num):
        next_value = seq[i - 1] + seq[i - 2]
        seq.append(next_value)

    if num in seq:
        print(f"The number {num} is Fibonacci !!")
    else:
        print(f"The number {num} is not Fibonacci !!")


num = 11
fib_check(num)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###To find max number from array which include negative values
def max_number(arr):
    max = 0
    n = len(arr)
    print("Length : ", n)
    for a in range(n):
        print("value from arr[a] :", arr[a])
        if arr[a] < 0:
            continue
        else:
            if arr[a] > max:
                max = arr[a]

        print(max)

    return max


arr = [22, 4, 55, -1, 6, 4, -200, 100]
max = max_number(arr)
print("Max number in array is :", max)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###To rotate the numbers in a list
def rev_arr(arr):
    print(arr)
    re = arr[::-1]
    return re
def rotate_ar(arr):
    i = 0
    x = arr.pop(i)
    print("Removed :", x)
    print("Array is now becomes :", arr)
    arr.append(x)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ro = rotate_ar(arr)
print("Rotated list is :", ro)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###To rotate all numbers in a list
def rev_arr(arr):
    print(arr)
    re = arr[::-1]
    return re

def rotate_ar(arr):
    i = 0
    for a in arr:
        x = arr.pop(i)
        # print("Removed :",x)
        arr.append(x)
        print("Array is now becomes :", arr)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ro = rotate_ar(arr)
re = rev_arr(arr)
print("Rotated list is :", ro)
print("Reverse list is :", re)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Split and rotate array/list
def split_arr(arr, k):
    x = arr[:k]
    print(x)
    y = arr[k:]
    print(y)
    return y + x


arr = [12, 10, 5, 6, 52, 36]
k = 2

new_arr = split_arr(arr, k)
print("Required arr : ", new_arr)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Fibonacci list till given number
def fibo(num):
    fib_lst = [0, 1]
    for i in range(len(fib_lst), num):
        next_value = fib_lst[i - 1] + fib_lst[i - 2]
        fib_lst.append(next_value)

    return fib_lst


fib = fibo(9)
print(f"fibonacci number is :", fib)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Verify the given array/list is monotonic
def mono(arr):
    arrAsc = []
    arrDsc = []

    arrAsc.extend(arr)
    arrAsc.sort()
    print(arrAsc)

    arrDsc.extend(arr)
    arrDsc.sort(reverse=True)
    print(arrDsc)

    if (arr == arrAsc or arr == arrDsc):
        print("Array is monotonic")
    else:
        print("Array is not monotonic")


arr = [34, 32, 4, 4]
mono(arr)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Print duplicates from the list
def countList(lst):
    arr = []
    for i in lst:
        count = 0
        for j in lst:
            if (i == j) & (j not in arr):
                count = count + 1
        if count > 1:
            arr.append(i)

    return arr


lst = [2, 4, 1, 5, 2, 6, 3, 2, 6, -1, -1]
arr = countList(lst)
print("Duplicates are :", arr)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Verify the string is palindrom
def palindrom(str):
    str1 = ""
    str1 = str[::-1]
    print(str1)
    if str == str1:
        print("String is palindrom !")
    else:
        print("String is not Palindrom !")


string = "malayalam"
palindrom(string)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###remove duplicates from string list and print uniq values
def remove_dups(str_lst):
    str_lst = list(set(str_lst))
    print("This is unique values list : ", str_lst)

    uniq_lst = []
    for str in str_lst:
        if str not in uniq_lst:
            uniq_lst.append(str)

    print(uniq_lst)


original_list = ['apple', 'orange', 'banana', 'apple', 'grape', 'banana']
remove_dups(original_list)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Count the Number of matching characters in a pair of string
def count_match(str1):
    count = 0
    match_lst = []
    for s in str1:
        if s in str2 and s not in match_lst:
            count = count + 1
            match_lst.append(s)
    print("Count of match is :", count)
    print("list of matching chars are :", match_lst)

str1 = 'abcdefd'
count_match(str1)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Print least frequency characters
def fequcy_count(str):
    least = []
    str_st = list(set(str))
    for s in str_st:
        x = str.count(s)
        if x < 2:
            least.append(s)
    print("Least fequncy chars are :", least)


test_str = "GeeksforGeeks"
fequcy_count(test_str)
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Print max frequency character with count in string
def fequcy_count(str):
    mx = 0
    str_st = list(set(str))
    for s in str_st:
        x = str.count(s)
        if x > mx:
            mx = x
            ch = s

    print(f"max fequncy chars is {ch} with count {mx}")


test_str = "GeeksforGeekkks"
fequcy_count(test_str)
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Check if string have special character
def special_char(str):
    sp_chars = []
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ' ']
    for s in str:
        if s in special_chars and s not in sp_chars:
            sp_chars.append(s)

    if sp_chars:
        print("String have these special characters :", sp_chars)
    else:
        print("String does not have any special character !!")


test_str = "GeeksForGeeks"
special_char(test_str)

#* ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Find words which are greater than given length in a string
def word_check(str, n):
    word_lst = str.split()
    big_word_lst = []
    for word in word_lst:
        if len(word) > n and word not in big_word_lst:
            big_word_lst.append(word)

    print(f"The list of words more than {n} chars are :", big_word_lst)


str = """hello geeks for geeks 
         is computer science portal"""
n = 5
word_check(str, n)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to split and join a string in python
def split_string(str):
    splt_lst = str.split()
    return splt_lst


def join_string(list_string):
    join_str = ' '.join(list_string)
    return join_str


str = """hello geeks for geeks 
         is computer science portal"""
splited_string = split_string(str)
print("Splited string is :", splited_string)
joined_string = join_string(splited_string)
print("Joined string is :", joined_string)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to check the given string is binary or not
def binary_check(str):
    count = 0
    for s in str:
        if s != '1' and s != '0':
            print(f"The given string is not binary since it contains {s}")
            count = count + 1
            break

    if count == 0:
        print(f"The string {str} is binary !!")


str = "010101"
binary_check(str)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to replace the duplicate words in a string
def replace_word(str, w):
    split_str = str.split()
    ind_list = []
    for word in split_str:
        count = 0
        for word1 in split_str:
            if word == word1:
                count = count + 1
                if count > 1:
                    ind = split_str.index(word1)
                    if ind not in ind_list:
                        ind_list.append(ind)

    for i in ind_list:
        split_str[i] = w
    string = ' '.join(split_str)
    print("After replacement the string is : ", string)


test_str = '''Gfg is best . Gfg also has Classes now. \ 
                Classes help understand better . '''
w = "thanks"
replace_word(test_str, w)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to count the occurences of each word in string
def count_words(str):
    split_words = str.split()
    uniq_words = list(set(split_words))
    print(uniq_words)
    for word in uniq_words:
        count = 0
        for word1 in split_words:
            if word == word1:
                count = count + 1
        print(f"count of {word} is :", count)


str = "my name is mahesh name is"
count_words(str)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to find uncoman words in 2 strings
def check_words(str1, str2):
    uncoman = []
    string_lst1 = str1.split()
    string_lst2 = str2.split()
    for s in string_lst1:
        count = 0
        if s not in string_lst2 and s not in uncoman:
            uncoman.append(s)

    print("Uncomman words are :", uncoman)


str1 = "my name is mahesh name"
str2 = "mahesh is good in testing"
check_words(str1, str2)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Bubble sort
def buble_sort(nums):
    l = len(nums)
    print("length of list is :", l)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                x = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = x
            else:
                continue
    print(nums)


nums = [3, 2, 8, 5, 6, 1, 9]
buble_sort(nums)

#* ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Remove empty lists from a list
def empty_lst(lst):
    lst1 = []
    for i in lst:
        if i != []:
            lst1.append(i)
        else:
            continue

    print(lst1)


lst = [5, 6, [], 3, [1], [], [], 9, [], 1]
empty_lst(lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Print Uniq values from lists in dictionary
def uniq_vals(test_dict):
    x = list(test_dict.values())
    y = []
    res = []
    for i in x:
        y.extend(i)
    for i in y:
        if i not in res:
            res.append(i)
    res.sort()
    print("Uniq values in dict are :", res)


test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
uniq_vals(test_dict)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Sum of all values in dictionary
def sum_all(test_dict):
    x = list(test_dict.values())
    sum = 0
    for i in x:
        sum = sum + i
    print("Sum of all values in dict : ", sum)


test_dict = {'a': 100, 'b': 200, 'c': 300}
sum_all(test_dict)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Remove a key from dictionary without exception
def sum_all(test_dict, n):
    print("Before remove operation dict :", test_dict)
    x = list(test_dict.keys())
    l = len(test_dict)
    for i in x:
        if i == n:
            test_dict.pop(i)

    if len(test_dict) == l:
        print(f"No {n} key present in dictionary")
    else:
        print("After remove operation dict :", test_dict)


n = 'Mani'
test_dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
sum_all(test_dict, n)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
###Sorting Dict	list using itemgetter and sorted functions
from operator import itemgetter


def sort_dict(test_dict):
    print("Before sorting :", test_dict)
    sort_list = sorted(test_dict, key=itemgetter('age'))
    print("After sorting : ", sort_list)

    sort_list = sorted(test_dict, key=itemgetter('age', 'name'))
    print("After sorting : ", sort_list)

    sort_list = sorted(test_dict, key=itemgetter('name'))
    print("After sorting : ", sort_list)


test_dict = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]
sort_dict(test_dict)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Check integer list in other integer list maitaining sequence
def list_check(A, B):
    l1 = map(str, A)
    l2 = map(str, B)
    x1 = list(l1)
    m1 = "".join(x1)

    x2 = list(l2)
    m2 = "".join(x2)

    if m1 in m2:
        print("True")
    else:
        print("False")


A = [1, 2]
B = [1, 2, 3, 1, 1, 2, 2]
list_check(A, B)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Find max counter(votes) with min alphabetic key in dictonary
def count_vote(votes):
    votes_dict = {}
    uniq_names = list(set(votes))
    for i in uniq_names:
        count = 0
        for j in votes:
            if i == j:
                count = count + 1
        votes_dict[i] = count
    print("All names voting is :", votes_dict)
    max_val = max(votes_dict.values())
    max_val_dict = {}
    for name in votes_dict:
        x = votes_dict[name]
        if x == max_val:
            max_val_dict.update({name: x})
    print("Max val :", max_val_dict)
    key_list = list(max_val_dict.keys())
    min_str = ""
    if len(key_list) > 1:
        for i in range(len(key_list) - 1):
            if len(key_list[i]) < len(key_list[i + 1]):
                min_str = key_list[i]
    else:
        for i in key_list:
            min_str = i

    print("The smallest name with max votes is :", min_str)


votes = ["john", "johnny", "jackie",
         "johnny", "john", "jackie",
         "jami", "jami", "john",
         "johnny", "johnny", "jami",
         "john", "jami"]

count_vote(votes)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Sort dictionary using keys
def sort_dict(myDict):
    key_list = list(myDict.keys())
    key_list.sort()
    print(key_list)
    sorted_dict = {}
    for key in key_list:
        sorted_dict[key] = myDict[key]

    print("Sorted dictionary is :", sorted_dict)


myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}
sort_dict(myDict)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Sort dictionary using values
def sort_dict(myDict):
    sorted_dict = sorted(myDict.items(), key=lambda x: x[1])
    print("This is list :", sorted_dict)
    sorted_dict = dict(sorted_dict)
    print("This is dictionary :", sorted_dict)


myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}
sort_dict(myDict)


###############
def test(dic):
    keys = list(dic.keys())
    values = list(dic.values())
    values.sort()
    # print(values)
    lst_final = []
    for i in values:
        for j in keys:
            if i == dic[j]:
                lst_final.append(j)

    print(lst_final)


dic = {"A": 2, "B": 1, "C": 0, "D": 4}
test(dic)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Binary search in list
def search(lst, n):
    lst.sort()
    l = 0
    u = len(lst)

    while l < u:
        mid = (l + u) // 2
        if lst[mid] == n:
            print(f"The {n} is found at position {mid}")
            break
        else:
            if lst[mid] < n:
                u = mid
            else:
                l = mid


lst = [3, 45, 9, 32, 100, 43]
n = 45
search(lst, n)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###split and print string in reverse order
def str_op(str):
    str1 = []
    str2 = []
    str3 = []
    mid = len(str) // 2
    count = 0
    for i in str:
        if count < mid:
            str1.append(i)
            count = count + 1
        elif count == mid:
            str2.append(i)
            count = count + 1
        elif count > mid:
            str3.append(i)
            count = count + 1
        else:
            break
    str_first = "".join(str1)
    str_sec = "".join(str2)
    str_third = "".join(str3)

    str_final = str_third + str_sec + str_first
    print(str_final)


str = "maheshdkharat"
str_op(str)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Find all subarrays from the list where the total of elements is 10. List will always be traversed sequentially
def sub_arr(list1):
    list2 = []
    n = len(list1)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + list1[j]
            if sum == 10:
                list2.append(list1[i:j + 1])

    print(list2)


list1 = [1, 2, 3, 2, 1, 1, 2, 3, 1, 2, 2]
sub_arr(list1)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###find least occured chars in given string using dictionary
def least_achr(str):
    count_dict = {}
    for i in str:
        count = 0
        for j in str:
            if i == j:
                count = count + 1
        count_dict[i] = count
    print(count_dict)
    mi = min(count_dict.values())
    ky = list(count_dict.keys())
    least = []
    for i in ky:
        if count_dict[i] == mi:
            least.append(i)

    print("Least occured char is :", least)


str = "thisistestehm"
least_achr(str)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Find the dictionay key present in given string else print invalid string
def search_str(str, dic1):
    dic1_keys = list(dic1.keys())
    ind = 0
    key = ""
    month = ""
    for i in dic1_keys:
        if i in str:
            ind = str.index(i)
            key = i
            month = dic1[key]

    if ind == 0:
        print("Invalid string !!")
    else:
        print(f"The key {key} positioned at {ind} = {month}")

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to combine lists present in list
def str_combine(str_lst):
    lst1 = []
    for i in str_lst:
        if type(i) == int:
            lst1.append(i)
        else:
            lst1.extend(i)

    print(lst1)


str_lst = [1, 2, [3, 4, 5], [6, 7]]
str_combine(str_lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Program to print combination of selected 2 string words
def dic_co(dic1, n, m):
    x = dic1[n]
    y = dic1[m]

    for i in x:
        for j in y:
            com = i + j
            print(com)


dic1 = {2: "abc", 3: "def", 4: "ghi"}
n = 3
m = 2
dic_co(dic1, n, m)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###program to create a sublist in list
def matrix_map(lst):
    matrix = []
    for i in range(len(lst)):
        list1 = []
        for row in lst:
            list1.append(row[i])
        matrix.append(list1)
    print(matrix)


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_map(my_matrix)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###write class >> function>> char count by taking input string from user
class Charecters:
    def __init__(self, str):
        self.count = 0
        self.str = str

    def count_chars(self):
        for i in self.str:
            self.count = self.count + 1

        print(f"Count of characters in {self.str} is {self.count}")

    def count_words(self):
        uniq_words = list(set(self.str))
        for i in uniq_words:
            count = 0
            for j in self.str:
                if i == j:
                    count += 1
            print(f"{i} = {count}")


print("Enter the string :")
str = input()

cl = Charecters(str)
cl.count_chars()
cl.count_words()

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Python class inheritance program
class Employee:
    no_of_emp = 0
    increment = 5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.increment * self.pay


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Tester(Employee):
    def __init__(self, first, last, pay, qa_tool):
        super().__init__(first, last, pay)
        self.qa_tool = qa_tool


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('mahesh', 'kharat', 50000)
emp_2 = Developer('Rihansh', 'kharat', 150000, 'Java')
emp_3 = Tester('Rohini', 'kharat', 250000, 'selenium')

mgr_1 = Manager('Drupat', 'kharat', 90000, [])
mgr_1.add_emp(emp_1)
mgr_1.add_emp(emp_2)

print("Number of employees created :", Employee.no_of_emp)

print(mgr_1.print_emp())

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###print patterns
class Pattern:
    def __init__(self, num):
        self.num = num

    def create_pattern(self):
        for i in range(self.num):
            for j in range(i + 1):
                print('', end=' ')
            for j in range(i, self.num):
                print('*', end=' ')
            print()
        for i in range(self.num):
            for j in range(i, self.num):
                print('', end=' ')
            for j in range(i + 1):
                print('*', end=' ')
            print()


num = int(input("Enter the range in number : "))
pat = Pattern(num)
print(pat.create_pattern())

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###2nd max number
def max_num(lst):
    max = 0
    max2 = 0
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    print(max)
    for i in range(len(lst)):
        if lst[i] < max and lst[i] > max2:
            max2 = lst[i]

    print(f"2nd max number is :", max2)


lst = [3, 5, 2, 8, 9]
max_num(lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Combine tuples by matching initials in tuples list
def tup_combine(lst):
    res = []
    lst1 = []
    for sub2 in lst:
        if sub2[0] not in lst1:
            lst1.append(sub2[0])
    print(lst1)
    for i in lst1:
        lst2 = []
        lst2.append(i)
        for j in lst:
            if i == j[0]:
                lst2.append(j[1])
        res.append(lst2)
    print(res)


lst = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
tup_combine(lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Bubble sort in list
def bubble_sort(nums):
    for j in range(len(nums) - 1, 0, -1):
        x = 0
        for i in range(j):
            if nums[i] > nums[i + 1]:
                x = 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    print(nums)


nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###Find 2nd largest number with negative numbers in list
def find_second_largest(example_list):
    max1 = float('-inf')
    max2 = float('-inf')

    for i in example_list:
        if i > max1:
            max1 = i

    for i in example_list:
        if i > max2 and i < max1:
            max2 = i

    print("Second largest number is :", max2)


example_list = [-10, -20, -4, -45, -99, -99]
find_second_largest(example_list)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###addition of two numbers from 2 different lists in reverse order
def solution(l1, l2):
    str1 = []
    for i in l1:
        i = str(i)
        str1.append(i)
        str2 = ''.join(str1)
        final1 = int(str2)

    str3 = []
    for i in l2:
        i = str(i)
        str3.append(i)
        str4 = ''.join(str3)
        final2 = int(str4)

    final3 = final1 + final2
    final4 = str(final3)
    f = final4[::-1]
    final = []
    for i in f:
        final.append(i)

    print(final)


l1 = [2, 4, 3]
l2 = [5, 6, 4]
solution(l1, l2)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

###print pyramid for given number
def pyramid(num):
    count = num
    for i in range(count):
        lst = []
        for j in range(count):
            lst.append(j)
        print(lst)
        count = count - 1


num = 5
pyramid(num)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

# Write a python program to find duplicate characters in the below list? list ['india', 'is', 'my', 'country']
def dup(lst):
    dups = []
    str = ''.join(lst)
    for i in str:
        count = 0
        for j in str:
            if i == j and i not in dups:
                count = count + 1
        if count > 1:
            dups.append(i)

    print(dups)


lst = ['india', 'is', 'my', 'country']
dup(lst)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

def prim(num):
    prim = []
    for i in range(1, num + 10):
        count = 0
        for j in range(2, int((i / 2) + 1)):
            if i % j == 0:
                count = count + 1

        if count == 0:
            prim.append(i)
    print(prim)

    if num in prim:
        print("Given number is prime")
    else:
        for i in prim:
            if i > num:
                print("The next prime is :", i)
                break


num = 11
prim(num)

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

# Write a python program to count the number of times a class is called in python?
class CounterClass:
    # Class attribute to store the count of instances
    instance_count = 0

    def __init__(self):
        # Increment the instance count each time a new object is created
        CounterClass.instance_count += 1

    @classmethod
    def get_instance_count(cls):
        # Class method to return the current count of instances
        return cls.instance_count


# Example usage
if __name__ == "__main__":
    # Creating instances of CounterClass
    obj1 = CounterClass()
    obj2 = CounterClass()
    obj3 = CounterClass()
    obj3 = CounterClass()

    # Print the number of times the class was instantiated
    print("Number of times CounterClass was called:", CounterClass.get_instance_count())

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

