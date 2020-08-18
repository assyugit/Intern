#coding:UTF-8
import sys
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='log監視')

parser.add_argument('-d','--day',help='更新期間閾値(日数指定)',default=7,type=int)
parser.add_argument('-f','--fname',help='結果ファイルパス',required=True)
parser.add_argument('-c','--check',help='logファイル最終行判定文字列',default='gdrive')
parser.add_argument('-s','--search',help='検索対象文字列',default='succeed')

args = parser.parse_args()

dt_now = datetime.now()
sys.stdin = file(args.fname)
log_line = sys.stdin.readline()

f = open("log_output.txt","w")

try:
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
except Exception:
 f.write("-9") #予期せぬエラー
 f.close()

if fresult == ftime:
 out = 0 #正常終了
elif fresult == -1 and ftime == 0:
 out = -1 #バックアップが取れてない
elif fresult == 0 and ftime == -2:
 out = -2 #更新日時が古い
else:
 out = -3 #バックアップ、更新日時、ともに不可

f.write(str(out))
f.close()
