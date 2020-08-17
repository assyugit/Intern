#coding:UTF-8
import sys
from datetime import datetime

dt_now = datetime.now()
log_line = sys.stdin.readline()

cnt = 1

while log_line:
 print log_line.strip()
 if cnt==1 or cnt==4:
  if "succeed" in log_line.strip():
   print "正常終了 : 0"
  else:
   print "以上終了 : 1"
 elif cnt==2:
  dt_p = log_line.strip()
  pdate = datetime.strptime(dt_p,'%Y-%m-%d-%H%M')
  td_m = dt_now - pdate
  if td_m.days < 7:
   print "正常終了 : 0"
  else:
   print "以上終了 : 1"

 log_line=sys.stdin.readline()
 if cnt ==4:
  cnt=0
 cnt+=1
