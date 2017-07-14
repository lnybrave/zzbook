#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime


def calcDays(strBeginTime, strEndTime):
    lstRetTime = []
    objBeginDatetime = datetime.datetime(int(strBeginTime[0 : 4]), int(strBeginTime[4 : 6]), \
            int(strBeginTime[6 : 8]), 0, 0)
    objEndDatetime = datetime.datetime(int(strEndTime[0 : 4]), int(strEndTime[4 : 6]), \
            int(strEndTime[6 : 8]), int(strEndTime[8 : 10]), int(strEndTime[10 : 12]))

    objTimedelta = datetime.timedelta(1)
    if objEndDatetime < objBeginDatetime:
        return lstRetTime

    strBeginDay = strBeginTime
    objDatetime = (objBeginDatetime + objTimedelta)
    if objDatetime >= objEndDatetime:
        strEndDay = strEndTime
    else:
        strEndDay = "%s2359" % (strBeginTime[0 : 8])

    lstRetTime.append([strBeginDay, strEndDay])

    while objDatetime <= objEndDatetime:
        strBeginDay = "%04d%02d%02d0000" % (objDatetime.year, objDatetime.month, objDatetime.day)
        strEndDay = "%04d%02d%02d2359" % (objDatetime.year, objDatetime.month, objDatetime.day)
        lstRetTime.append([strBeginDay, strEndDay])
        objDatetime = (objDatetime + objTimedelta)

    lstRetTime[-1][1] = strEndTime
    return lstRetTime

#减少天数，例如：传入 2015-08-06 23:00:00和1 返回 2015-08-05 23:00:00
def subtractDays(strTime, iDays):
    strTime = str(strTime)
    strTime = strTime.replace(":", '').replace("-", '').replace(" ",'')
    objDatetime = datetime.datetime(int(strTime[0 : 4]), int(strTime[4 : 6]), \
            int(strTime[6 : 8]), int(strTime[8 : 10]), int(strTime[10 : 12]), int(strTime[12 : ]))
    objTimedelta = datetime.timedelta(iDays)
    objDatetime2 = (objDatetime - objTimedelta)

    strRetTime =  "%04d-%02d-%02d %02d:%02d:%02d" % (objDatetime2.year, objDatetime2.month, objDatetime2.day, \
        objDatetime2.hour, objDatetime2.minute, objDatetime2.second)
    return strRetTime

#增加天数，例如：传入 2015-08-06 23:00:00和1 返回 2015-08-07 23:00:00
def addDays(strTime, iDays):
    strTime = str(strTime)
    strTime = strTime.replace(":", '').replace("-", '').replace(" ",'')
    objDatetime = datetime.datetime(int(strTime[0 : 4]), int(strTime[4 : 6]), \
            int(strTime[6 : 8]), int(strTime[8 : 10]), int(strTime[10 : 12]))
    objTimedelta = datetime.timedelta(iDays)
    objDatetime2 = (objDatetime + objTimedelta)

    strRetTime = "%04d-%02d-%02d %02d:%02d:%02d" % (objDatetime2.year, objDatetime2.month, objDatetime2.day, \
        objDatetime2.hour, objDatetime2.minute, objDatetime2.second)
    return strRetTime

# #减少月数，例如：传入 2015-08-06 23:00:00和1 返回 2015-07-05 23:00:00
# def subtractMonths(strTime, iMonths):
#     strTime = str(strTime)
#     strTime = strTime.replace(":", '').replace("-", '').replace(" ",'')
#     objDatetime = datetime.datetime(int(strTime[0 : 4]), int(strTime[4 : 6]), \
#             int(strTime[6 : 8]), int(strTime[8 : 10]), int(strTime[10 : 12]), int(strTime[12 : ]))
#
#     objTimedelta = datetime.timedelta(iMonths)
#     objDatetime2 = (objDatetime - objTimedelta)
#
#     strRetTime =  "%04d-%02d-%02d %02d:%02d:%02d" % (objDatetime2.year, objDatetime2.month, objDatetime2.day, \
#         objDatetime2.hour, objDatetime2.minute, objDatetime2.second)
#     return strRetTime

#时间对象字符串,例如：传入None 返回"" 传入1980-07-12 23:00:00 返回"1980-07-12 23:00:00"
def time2str(time):
    if time == None:
        return ""

    sTime = str(time)
    sTime = sTime.strip()
    if len(sTime) >= 19:
        sTime = sTime[:19]
    return sTime

#增加小时,例如，传入 01:30和02:40 返回 04:10
def addHours(time1, time2):
    if not time1:
        time1 = "00:00"

    if not time2:
        time2 = "00:00"

    time11, time12 = time1.split(":")
    time11 = int(time11)
    time12 = int(time12)

    time21, time22 = time2.split(":")
    time21 = int(time21)
    time22 = int(time22)

    t1 = datetime.timedelta(hours=time11, minutes=time12)
    t2 = datetime.timedelta(hours=time21, minutes=time22)

    t = t1 + t2
    hour, minute = seconds2Hour(t.total_seconds())
    result = "%02d:%02d" % (abs(hour), abs(minute))
    return result

#增加小时列表,例如，传入 [01:30,02:40] 返回 04:10
def addHoursList(lstTime):
    sAdd = "00:00"
    for sTmp in lstTime:
        sAdd = addHours(sAdd, sTmp)

    return sAdd

def averageHours(time1, num):
    if not time1:
        time1 = "00:00"

    time11, time12 = time1.split(":")
    time11 = int(time11)
    time12 = int(time12)

    t = datetime.timedelta(hours=time11, minutes=time12)
    hour, minute = seconds2Hour(t.total_seconds() / num)
    result = "%02d:%02d" % (abs(hour), abs(minute))
    return result

def seconds2Hour(seconds):
    if seconds < 0:
        minute = seconds / 60
        tmphour, tmpminute = divmod(abs(minute), 60)
        return tmphour * -1, tmpminute * -1
    else:
        minute = seconds / 60
        return divmod(minute, 60)

if __name__== "__main__":
    #lstTime = objTime.calcDays('200607250830','200607271520')
    lstTime = subtractDays('20060725083022', 14)
    print lstTime