# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

the_date = list(map(int, input().split()))

month = the_date[0]
day = the_date[1]
year = the_date[2]

day_int = calendar.weekday(year, month, day)

if day_int == 0:
    print("MONDAY")
elif day_int == 1:
    print("TUESDAY")
elif day_int == 2:
    print("WEDNESDAY")
elif day_int == 3:
    print("THURSDAY")
elif day_int == 4:
    print("FRIDAY")
elif day_int == 5:
    print("SATURDAY")
elif day_int == 6:
    print("SUNDAY")
