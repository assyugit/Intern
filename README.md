# インターンシップ課題
logの監視システム
# 使用言語
Python2.7.16  
# 使用ライブラリ
import sys  
from datetime import datetime  
import argparse
# オプション・引数
-f | --fname required=True  
  結果ファイルパス 必須引数  
-d | --day type=int default=7  
  更新期間期間閾値  
-c | --check default=gdrive  
  最終行判定文字列  
-s | --search default=succeed  
  検索対象文字列(成功表現文字列)
# 使い方
1. スクリプトの実行(オプションで結果ファイルパス、更新期間閾値、最終行判定文字列、成功表現文字列を指定)  
2. 結果が"log_output.txt"として出力される
# 参考文献
1.[今日からはじめるGitHub 〜 初心者がGitをインストールして、プルリクできるようになるまでを解説](https://employment.en-japan.com/engineerhub/entry/2017/01/31/110000)  
2.[初心者でもできるPython入門 – はじめての学習まとめ](https://codeaid.jp/py-novice/)  
3.[Python datetime 日付の計算、文字列変換をする方法 strftime, strptime【決定版】](https://qiita.com/7110/items/4ece0ce9be0ce910ee90)  
4.[Pythonで現在時刻・日付・日時を取得](https://note.nkmk.me/python-datetime-now-today/)  
5.[ArgumentParserの使い方を簡単にまとめた](https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0#%E5%BF%85%E9%A0%88%E5%BC%95%E6%95%B0)  
6.[Pythonの例外処理（try, except, else, finally）](https://note.nkmk.me/python-try-except-else-finally/)
