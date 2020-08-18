#coding:UTF-8
import sys
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='log監視')    # 2. パーサを作る

parser.add_argument('-d','--day',help='更新期間閾値',default=7,type=int)
parser.add_argument('-f','--fname',help='結果ファイルパス',required=True)
parser.add_argument('-c','--check',help='logファイル最終行判定文字列',default='gdrive')

args = parser.parse_args()

dt_now = datetime.now()
sys.stdin = file(args.fname)
log_line = sys.stdin.readline()


while log_line:
 if args.check in log_line.strip():
  if "succeed" in log_line.strip():
   fresult = 0
  else:
   fresult = -1
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

if fresult == ftime:
 out = 0
elif fresult == -1 and ftime == 0:
 out = -1
elif fresult == 0 and ftime == -2:
 out = -2
else:
 out = -3

f = open("log_output.txt","w")
f.write(str(out))
f.close()
