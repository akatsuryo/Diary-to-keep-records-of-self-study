import os
import cv2
from pathlib import Path

def label1(right_polygon_folder,right_folder):
    # 出力先のラベルフォルダのパス
    
    labels_folder = os.path.join(right_folder, "right_label")
    Path(labels_folder).mkdir(parents=True, exist_ok=True)

    # ポリゴン画像を読み取る
    polygon_images = [img for img in os.listdir(right_polygon_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]

    for img_file in polygon_images:
        image_path = os.path.join(right_polygon_folder, img_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # ポリゴンの座標抽出
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        height, width = image.shape

        # 相対座標の辞書
        relative_coordinates = {}

        for i, contour in enumerate(contours):
            # ポリゴンの各頂点の相対座標を計算
            points = [pt[0] for pt in contour]
            relative_points = [(pt[0] / width, pt[1] / height) for pt in points]
            relative_coordinates[i] = relative_points

        # 相対座標をtxtファイルに保存
        txt_filename = os.path.splitext(img_file)[0] + ".txt"
        txt_path = os.path.join(labels_folder, txt_filename)

        with open(txt_path, 'w') as f:
            for key, coords in relative_coordinates.items():
                coords_str = ', '.join([f"({x:.4f}, {y:.4f})" for x, y in coords])
                f.write(f"{key}: [{coords_str}]\n")

    print(f"相対座標の抽出と保存が完了しました。保存先: {labels_folder}")


