#coding:UTF-8
import sys
from datetime import datetime

dt_now = datetime.now()
log_line = sys.stdin.readline()

cnt = 1
flag = 0

while log_line:
 print str(cnt) + "行目"
 print log_line.strip()
 if cnt==1 or cnt==4:
  if "succeed" in log_line.strip():
   print "正常終了 : 0"
   if flag==0:
    succes1=0
    flag=1
   elif flag==1:
    succes2=0
    flag=0
  else:
   print "以上終了 : 1"
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
  if td_m.days < 7:
   print "正常終了 : 0"
   time_dif=0
  else:
   print "以上終了 : 1"
   time_dif=1

 log_line=sys.stdin.readline()
 if cnt ==4:
  cnt=0
  print "結果"
  if succes1==0 and succes2==0 and time_dif==0:
   print "正常終了 : 0"
  else:
   print "異常終了 : 1"
 cnt+=1
