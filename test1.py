# import pymysql
#
# conn = pymysql.connect(host='localhost', user='root', password='password', db='test')
# cursor = conn.cursor()
#
# query = '''select * from customer
# where ID = 123 '''
#
# cursor.execute(query)
# result = cursor.fetchall()
# exepected = []
#
# assert result, exepected
#
# conn.close()
import re

# def prim_check(num):
#     check = True
#     if num == 0 or num == 1:
#         print("Entered 0 or 1 which is always composite number !!")
#     else:
#         for i in range(2, (int(num/2)+1)):
#             if num%i == 0:
#                 check = False
#
#         if check == False:
#             print("Number is not prime !")
#         else:
#             print("Number is prime !!")
#
# num = int(input("Enter any number : "))
# prim_check(num)
#
# string = "ThisIsGeeksforGeeks !, 123"
#
# total_upper_chars = len(re.findall(r"[A-Z]", string))
# total_lower_chars = len(re.findall(r"[a-z]", string))
# total_digits = len(re.findall(r"[0-9]", string))
# total_special_chars = len(re.findall(r"[!,@#$%^&*()_+=|]", string))
# print("Upper chars :", total_upper_chars)
# print("Lower chars :", total_lower_chars)
# print("Digits :", total_digits)
# print("Special chars :", total_special_chars)

s1 = "mahesh"
s2 = "ROHINI"

s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length > s2_length else s2_length
result = ""

s2 = s2[::-1]

for i in range(length):
    if i < s1_length:
        result = result+s1[i]
    if i < s2_length:
        result = result+s2[i]

print(result)

