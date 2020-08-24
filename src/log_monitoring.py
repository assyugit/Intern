#coding:UTF-8
import sys
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='log監視')

parser.add_argument('-d','--day',help='更新期間閾値(日数指定)',default=7,type=int)
parser.add_argument('-f','--fname',help='結果ファイルパス',required=True)
parser.add_argument('-c','--check',help='logファイル最終行判定文字列',default='gdrive')
parser.add_argument('-s','--search',help='検索対象文字列',default='succeed')

args = parser.parse_args()

try:
 dt_now = datetime.now()
 sys.stdin = file(args.fname)
 log_line = sys.stdin.readline()

 while log_line:
  if args.check in log_line.strip():
   if args.search in log_line.strip():
    fresult = 0
    break
   else:
    fresult = -1
    break
  try:
   dt_p = datetime.strptime(log_line.strip(),'%Y-%m-%d-%H%M')
   t_dif = dt_now - dt_p
   if t_dif.days < args.day:
    ftime = 0
   else:
    ftime = -2
  except ValueError:
   pass

  log_line = sys.stdin.readline()

 if fresult == 0 and ftime == 0:
  #sys.exit(0)
 elif fresult == -1 and ftime == 0:
  sys.exit(1)
 elif fresult == 0 and ftime == -2:
  sys.exit(2)
 elif fresult == -1 and ftime == -2:
  sys.exit(3)

except Exception:
 sys.exit(9)
