# -*- coding: utf-8 -*-
"""
程式名稱:閏年判斷程式
題目要求:
輸入西元年(4位數的整數year)判斷是否為閏年
條件1.逢4閏(除4可整除)而且逢100不閏(除100不可整除)
條件2.逢400閏(除400可整除)
滿足兩個條件之一即是閏年
"""
year = int(input("請輸入西元年份:"))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("{0}是閏年".format(year))
else:
    print("{0}是平年".format(year))