"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/calendar-module/problem
"""

import calendar

if __name__ == "__main__":
    date_list = list(map(int, input().split()))
    month, date, year = date_list[0], date_list[1], date_list[2]
    
    day = calendar.weekday(year, month, date)  # Get the weekday corresponding to the day
    day_name = list(calendar.day_name)[day] # Index it from the day_name array
    print(day_name.upper())
