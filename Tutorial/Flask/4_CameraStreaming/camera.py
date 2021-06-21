import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # read()は、二つの値を返すので、success, imageの2つ変数で受けています。
        # OpencVはデフォルトでは raw imagesなので JPEGに変換
        # ファイルに保存する場合はimwriteを使用、メモリ上に格納したい時はimencodeを使用
        # cv2.imencode() は numpy.ndarray() を返すので .tobytes() で bytes 型に変換
        success, image = self.video.read()
        if success == True:
                ret, jpeg = cv2.imencode('.jpg', image)
        # self.video.read fail時何も返さないと復帰しないため静止画を返す
        # ちなみにfailになるのは複数のブラウザから表示した時
        else:
                image = cv2.imread('/home/pi/Picture/raspi.png', cv2.IMREAD_GRAYSCALE)
                ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
