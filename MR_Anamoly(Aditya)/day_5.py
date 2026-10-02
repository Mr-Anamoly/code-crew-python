
#lets play with date and time only python

#hashtag digital time travel

days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]
days_28 = [2]

year = int(input("Enter the year(YYYY): "))
month = int(input("Enter the month no.(1-12): "))
date = int(input("Enter the date(1-31): "))

print(f"\nThe date you entered is: {date}/{month}/{year}\n")
print(f"Date to travel to in future/past...\n")

year_travel = int(input("Enter the year to travel to(YYYY): "))
month_travel = int(input("Enter the month no. to travel to(1-12): "))
date_travel = int(input("Enter the date to travel to(1-31): "))


if year_travel < year:
    print(f"\nYou are travelling to the past\n")
    year_diff = year - year_travel
    #day logi.....

elif year_travel > year:
    print(f"\nYou are travelling to the future\n")
    year_diff = year_travel - year

#### in progress question; leap year logic + date*time logic + no. of days logic......intresting


  