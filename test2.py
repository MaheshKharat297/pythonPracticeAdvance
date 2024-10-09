lst = [5,8,19,26,13]
def myfunc(lst):
    x2 = []
    for i in lst:
        x = lambda i:i*3
        x2.append(x(i))
    print(x2)

myfunc(lst)


# # x = lst[4:4]
# # print(x)
# #
# # for _ in lst:
#
# def second_lsrge(lst):
#     max = 0
#     for i in lst:
#         if i > max:
#             max = i
#     lst.remove(max)
#     mx = 0
#     for i in lst:
#         if i > mx:
#             mx = i
#     print(f"2nd largest : {mx}")
#
# second_lsrge(lst)


#dic1 = {"mahesh":31, "ankita":23, "anita":67}
#
# def create_dic(names, numbers):
#     dic = {}
#     for i in range(len(names)):
#         dic[names[i]] = numbers[i]
#
#     print(dic)
#
# names = []
# numbers = []
# for i in range(3):
#     name = input("Enter name:")
#     names.append(name)
#     number = int(input("Enter number:"))
#     numbers.append(number)
#
# create_dic(names, numbers)
#
#
