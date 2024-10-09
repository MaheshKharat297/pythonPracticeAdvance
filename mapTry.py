# def double(n):
#     return n+n
#
# numbers = [1,2,3,4]
#result = map(double, numbers)

#print(list(result))

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
# numbers = [1,2,3,4,5,6]
# x = list(filter(lambda a: a % 2 == 0, numbers))
# print(x)
#
# city = ["pune", "mumbai", "jaipur", "goa"]
# sorted_city = sorted(city, key=lambda x: len(x))
# print(sorted_city)
