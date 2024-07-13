# -*- coding: utf-8 -*-
"""
时间格式类
"""


class _DateFormat:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        if month < 1 or month > 12:
            print("month must be between 1 and 12")
        if month in [4, 6, 9, 11]:
            if day > 30:
                print("day must be between 1 and 30")
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                if day > 29:
                    print("day must be between 1 and 29")
            else:
                if day > 28:
                    print("day must be between 1 and 28")
        else:
            if day > 31:
                print("day must be between 1 and 31")
        if hour > 23:
            print("hour must be between 0 and 23")
        if minute > 59:
            print("minute must be between 0 and 59")
        if second > 59:
            print("second must be between 0 and 59")

    def get(self):
        return self.year, self.month, self.day, self.hour, self.minute, self.second

    def iadd(self, month: int = 0, day: int = 0, hour: int = 0, minute: int = 0, second: int = 0):
        pass

    def isub(self, month: int = 0, day: int = 0, hour: int = 0, minute: int = 0, second: int = 0):
        pass

    def ceil(self,unit:str):
        """
        取整，unit为单位
        y年，m月，d日，h时，m分，s秒
        """
        pass

    def __eq__(self, other: "_DateFormat"):
        pass

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}"

    def __copy__(self):
        return _DateFormat(self.year,self.month,self.day,self.hour,self.minute,self.second)