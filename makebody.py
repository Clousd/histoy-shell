import time
import datetime
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

def bodystr():
    loveday = datetime.datetime(2018, 5, 28)
    dayCount = (datetime.datetime.now() - loveday).days+1

import  sxtwl
lunar = sxtwl.Lunar()
day = lunar.getDayBySolar(1993, 2, 26)
print("公历:", day.y, "年", day.m, "月", day.d, "日")
print  (u"公历:", day.y, u"年", day.m, u"月", day.d, u"日")
if day.Lleap:
    print(u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
else:
    print (u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
day1 = lunar.getDayByLunar(1993, 2, 26 , False) 
print("公历:", day1.y, "年", day1.m, "月", day1.d, "日")
if day1.Lleap:
    print("润", ymc[day1.Lmc], "月", rmc[day1.Ldi], "日")
else:
    print(ymc[day1.Lmc], "月", rmc[day1.Ldi], "日")

#print("儒略日:JD", sxtwl.J2000 + day.d0)
#print("星期", numCn[day.week])

#print(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], "年", Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], "月",\
#        Gan[day.Lday2.tg], Zhi[day.Lday2.dz], "日")

#print("距冬至", day.cur_dz, "天")
#print("距夏至", day.cur_xz, "天")
#print("距立秋", day.cur_lq, "天")
#print("距芒种", day.cur_mz, "天")
#print("距小暑", day.cur_xs, "天")