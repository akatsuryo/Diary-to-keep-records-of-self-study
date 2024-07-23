import os
import shutil
import cv2

def half_image(simple_path):
    data_remake = "data_remake"
    left_folder = os.path.join(data_remake, "left")
    right_folder = os.path.join(data_remake, "right")

    # 必要なフォルダが存在しない場合は作成
    for folder in [data_remake, left_folder, right_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # simple_pathフォルダ内の全ての画像ファイルを取得
    images = [img for img in os.listdir(simple_path) if img.endswith(('.png', '.jpg', '.jpeg'))]

    for image in images:
        # 画像のフルパスを取得
        img_path = os.path.join(simple_path, image)
        
        # 画像を読み込み
        simple_image = cv2.imread(img_path)
        
        if simple_image is None:
            print(f"{img_path} は無効な画像です。")
            continue
        
        # 画像の幅と高さを取得
        height, width = simple_image.shape[:2]
        
        # 画像を左右に分割
        left_image = simple_image[:, :width // 2]
        right_image = simple_image[:, width // 2:]
        
        # 左側の画像をleftフォルダにコピーして保存
        left_img_path = os.path.join(left_folder, image)
        cv2.imwrite(left_img_path, left_image)
        
        # 右側の画像をrightフォルダにコピーして保存
        right_img_path = os.path.join(right_folder, image)
        cv2.imwrite(right_img_path, right_image)
        
        # 画像をdata_remakeフォルダに移動
        shutil.move(img_path, os.path.join(data_remake, image))

    print("全ての画像が処理されました。")

# 分割処理したい画像フォルダのパスを入力

