#coding:UTF-8
import sys
import os
from datetime import datetime

update_day = input("update day >>>")
dt_now = datetime.now()
sys.stdin = file(raw_input("update check File name>>>"))
log_line = sys.stdin.readline()
cnt = 1
flag = 0

while log_line:
 if cnt==1 or cnt==4:
  if "succeed" in log_line.strip():
   #正常終了 : 0
   if flag==0:
    succes1=0
    flag=1
   elif flag==1:
    succes2=0
    flag=0
  else:
   #異常終了 : 1
   if flag==0:
    succes1=1
    flag=1
   elif flag==1:
    succes2=1
    flag=0

 elif cnt==2:
  dt_p = log_line.strip()
  pdate = datetime.strptime(dt_p,'%Y-%m-%d-%H%M')
  td_m = dt_now - pdate
  if td_m.days < update_day:
   #正常終了 : 0
   time_dif=0
  else:
   #異常終了 : 1
   time_dif=1

 log_line=sys.stdin.readline()
 if cnt ==4:
  cnt=0
  if succes1==0 and succes2==0 and time_dif==0:
   #正常終了 : 0
   print 0
  else:
   #異常終了 : 1
   print 1
 cnt+=1
