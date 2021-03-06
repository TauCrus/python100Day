# 判断指定年月日的这一年是第几天


def is_leap_year(year):
    '''
    判断指定年份是不是闰年
    param  year： 年份
    return ：闰年返回True 平年返回False
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天
    param year 年
    param month 月
    param date 日
    return 第几天
    '''

    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]

    print(days_of_month)
    total = 0

    for i in range(month-1):
        total += days_of_month[i]
    return total + date


def main():
    print(which_day(2013, 2, 12))
    print(which_day(2017, 6, 12))
    print(which_day(2018, 4, 8))
    print(which_day(2019, 5, 20))
    print(which_day(2020, 1, 1))


if __name__ == "__main__":
    main()
