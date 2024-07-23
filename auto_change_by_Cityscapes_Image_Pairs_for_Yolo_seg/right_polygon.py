import os
import cv2
from pathlib import Path

def right_polygon(mask_folder):
    # 出力ディレクトリの作成
    data_remake='data_remake'
    right=os.path.join(data_remake,'right')
    polygon_folder = os.path.join(right, "right_polygon")
    Path(polygon_folder).mkdir(parents=True, exist_ok=True)

    # マスク画像を読み取る
    mask_images = [img for img in os.listdir(mask_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    polygon_images = []

    for img_file in mask_images:
        image_path = os.path.join(mask_folder, img_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # 二値化処理
        _, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        # 輪郭を検出し、ポリゴンに近似する
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_polygons = [cv2.approxPolyDP(contour, 2, True) for contour in contours]

        # 元の画像をカラーで読み込み
        image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        # ポリゴンを画像に描画
        for polygon in contour_polygons:
            cv2.drawContours(image_color, [polygon], 0, (0, 255, 0), 2)

        # ポリゴン画像の保存パス
        polygon_image_path = os.path.join(polygon_folder, img_file)
        cv2.imwrite(polygon_image_path, image_color)
        

    print("処理が完了しました。polygon画像は {} に保存されています。".format(polygon_folder))
