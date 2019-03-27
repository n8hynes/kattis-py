import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def month_to_day(month):
    days = 0
    if month > 1: days += 31 #JAN
    if month > 2: days += 28 #FEB
    if month > 3: days += 31 #MAR
    if month > 4: days += 30 #APR
    if month > 5: days += 31 #MAY
    if month > 6: days += 30 #JUN
    if month > 7: days += 31 #JUL
    if month > 8: days += 31 #AUG
    if month > 9: days += 30 #SEP
    if month > 10: days += 31 #OCT
    if month > 11: days += 30 #NOV
    return days

def day_num_to_str(days):
    day_of_week = days % 7
    if (day_of_week == 0): return "Wednesday"
    if (day_of_week == 1): return "Thursday"
    if (day_of_week == 2): return "Friday"
    if (day_of_week == 3): return "Saturday"
    if (day_of_week == 4): return "Sunday"
    if (day_of_week == 5): return "Monday"
    if (day_of_week == 6): return "Tuesday"

def main():
    day, month = [ int(x) for x in input().split() ]
    total_days = day + month_to_day(month)
    print(day_num_to_str(total_days))

main()
