def get_month_name(month_num):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_num < 1 or month_num > 12:
        return "Invalid month"
    else:
        return month_list[month_num-1]

print("==================================")
print("\t\t2022 CALENDAR")
print("==================================")

month = int(input("Enter month [1-12]: "))
year = 2022

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12:
    print("Invalid month")
else:
    print("\n", get_month_name(month), 2022)
    print("Sun  Mon  Tue  Wed  Thu  Fri  Sat")
    # calculate the day of the week of the first day of the month
    first_day = (1 + sum(days[:month-1]) + (year-1) + ((year-1)//4) - ((year-1)//100) + ((year-1)//400)) % 7
    # print the calendar
    for i in range(first_day):
        print("    ", end=" ")
    for i in range(1, days[month-1]+1):
        print("%2d  " % i, end=" ")
        if (first_day + i) % 7 == 0:
            print()
