#coding:UTF-8
import sys

log_line = sys.stdin.readline()

cnt=1

while log_line:
 print log_line.strip()
 if "succeed" in log_line.strip():
  print "正常終了 : 0"
 else:
  print "以上終了 : 1"
 log_line=sys.stdin.readline()
