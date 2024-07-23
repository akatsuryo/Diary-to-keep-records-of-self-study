import os
import cv2
import numpy as np

def right_mask(right_folder):
    # 分割後のデータのパス（右がセグメント）
    mask_folder = os.path.join(right_folder, "right_mask")

    # セグメントから道に関するRGB値を指定
    road_color = np.array([128, 64, 128])
    tolerance = 10  # 許容する色の差

    # データセットのセグメント画像の読み取り
    right_images = [img for img in os.listdir(right_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]

    # マスク用フォルダがなければ作成
    if not os.path.exists(mask_folder):
        os.makedirs(mask_folder)

    # 取得した画像リストをfor文で1つずつ処理
    for img_name in right_images:
        # 画像のフルパスを取得
        img_path = os.path.join(right_folder, img_name)
        # 画像の読み込み
        image = cv2.imread(img_path)
        # マスクの初期化 (初期値は全て0)
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        # 色の許容範囲内でマスクを作成
        min_color = road_color - tolerance
        max_color = road_color + tolerance
        # 道のRGB値と等しいピクセルに対して1をセット
        mask[np.all((image >= min_color) & (image <= max_color), axis=-1)] = 1

        # マスク画像の保存パス
        mask_path = os.path.join(mask_folder, img_name)
        # マスク画像の保存
        cv2.imwrite(mask_path, mask * 255)  # 0と1の値を255倍して保存

    print("処理が完了しました。マスク画像は {} に保存されています。".format(mask_folder))


