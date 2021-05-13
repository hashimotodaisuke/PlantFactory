import sys # 引数を取得するためモジュール
from sense_hat import SenseHat

args = sys.argv # sys.argvはlist
#args[0]には実行ファイルがフルパスで入る
if len(args) == 1:
   args[1] = 'Input Something' 
sh=SenseHat()
sh.show_message(args[1])


