class CountOccur:
    count = 0

    def __init__(self):
        CountOccur.count += 1

    @classmethod
    def count_method(cls):
        return cls.count

if __name__ == "__main__":
    obj1 = CountOccur()
    obj2 = CountOccur()
    obj3 = CountOccur()
    print("Count class called :", CountOccur.count_method())
