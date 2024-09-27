def pyramid(num):
    for i in range(num):
        for j in range(i, num):
            print('', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        print()

def reversePyramid(num):
    for i in range(num):
        for j in range(i+1):
            print('', end=' ')
        for j in range(i, num):
            print('*', end=' ')
        print()
def leftLandedPyramid(num):
    for i in range(num):
        for j in range(i+1):
            print('*', end=' ')
        for j in range(i, num):
            print('', end=' ')
        print()
    for i in range(num):
        for j in range(i, num-1):
            print('*', end=' ')
        for j in range(i+1):
            print('', end=' ')
        print()
def rightLandedPyramid(num):
    for i in range(num):
        for j in range(i, num):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
        print()
    for i in range(num):
        for j in range(i+2):
            print(' ', end=' ')
        for j in range(i, num-1):
            print('*', end=' ')
        print()

num = int(input("Please enter max length of pyramid : "))

# reversePyramid(num)
# pyramid(num)
# leftLandedPyramid(num)
rightLandedPyramid(num)
