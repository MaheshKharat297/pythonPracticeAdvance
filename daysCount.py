
def find_leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        leap_year = True
    elif year % 4 == 0 and year % 100 != 0:
        leap_year = True
    else:
        leap_year = False

    return leap_year

def count_month_days(month, leap_year):
    if leap_year == True and month == 2:
        days = 29
    elif leap_year == False and month == 2:
        days = 28
    elif month < 8 and month % 2 == 0:
        days = 30
    elif month % 2 != 0 and month > 8:
        days = 30
    else:
        days = 31

    return days

def month_in_word(month):
    month_dic = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
                 6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
                 11: "November", 12: "December"}
    for i in month_dic:
        if i == month:
            month_word = month_dic[i]

    return month_word

if __name__ == "__main__":

    year = int(input("Enter Year : "))
    month = int(input("Enter month in number : "))

    if month <= 12 and month > 0 and year > 0:
        month_word = month_in_word(month)
        leap_year = find_leap_year(year)
        days = count_month_days(month, leap_year)

        if leap_year == True:
            print(f"The {year} is Leap year !!!!")

        print(f"Days in month {month_word} of year {year} is : {days}")

    else:
        print("Invalid input !!")

