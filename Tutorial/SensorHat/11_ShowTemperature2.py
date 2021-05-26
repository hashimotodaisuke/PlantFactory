from time import sleep
'''
sleepについて
pythonの不動小数点の情報はsys.float_infoで得ることが出来る
sys.float_info.max  1.7976931348623157e+308
sys.float_info.min  2.2250738585072014e-308
なので、sleepの時間指定の最小は2.2250738585072014e-308まで指定可能
(これより小さい数字を設定してもエラーとなることもない)
ただし、本当に精度が出ているかというと別問題である
Windowsのような非リアルタイムOSの場合、sleepできる最小間隔は10ms程度
ラズパイのようなubuntaベースのLinuxの場合、sleepできる最小間隔は1ms程度になります。
'''

from sense_hat import SenseHat

sh = SenseHat()
while True:
    temp = sh.humidity
    message = "{0:.1f}".format(temp)
    for moji in message:
        sh.show_letter(moji)
        sleep(1)

