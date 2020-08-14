#coding:UTF-8
#import datetime
from datetime import datetime

dt_now = datetime.now()
print dt_now

dt_p = "2020-08-09-1506"
tdate = datetime.strptime(dt_p,'%Y-%m-%d-%H%M')
print tdate

td_m = dt_now - tdate
print td_m
