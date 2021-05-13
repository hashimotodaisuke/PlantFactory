from sense_hat import SenseHat
import time

sh = SenseHat()
while True:
    # 磁気センサの生データ。Dicitonary型
    raw = sh.get_compass_raw()
    x_val = round(float(raw['x']),2)
    y_val = round(float(raw['y']),2)
    z_val = round(float(raw['z']),2)
    
    
    # 北からの位置を取得。加速度センサと磁気センサの値から計算している。範囲は0〜360、単位は度。0が北、180が南。
    # 値はゆっくり変化していく、方位磁石のほうが精度が良い
    north = sh.get_compass()
    print("North: %s (x=%s, y=%s, z=%s)" %(north, x_val, y_val, z_val))
    time.sleep(1)
