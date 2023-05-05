import calendar


def main():
    date_str = input("Enter a date (dd/mm/yyyy): ")
    day, month, year = map(int, date_str.split('/'))
    # weekday() function returns the day of the week as an integer where Monday is 0 and Sunday is 6
    weekday_num = calendar.weekday(year, month, day)
    # weekday_name[] list contains the name of the weekdays starting from Monday
    weekday_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(weekday_name[weekday_num])


if __name__ == '__main__':
    main()
