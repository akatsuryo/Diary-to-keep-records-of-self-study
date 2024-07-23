from half_image import half_image
from right_mask import right_mask
from right_polygon import right_polygon
from label1 import label1
from label2 import maxlabel
from label3 import maxlabel_change
import os

# 分割処理の呼び出し
simple_path = input('分割処理したい画像フォルダのパスを教えてください：')
half_image(simple_path)

# 分割後のデータのパス（左は普通の画像、右がセグメント）
data_remake = 'data_remake'
right_folder = os.path.join(data_remake, "right")

# マスク処理関数の実行
right_mask(right_folder)
#マスク処理後の画像データパス
right_mask_folder=os.path.join(right_folder,"right_mask")


# ポリゴン化処理の実行
right_polygon(right_mask_folder)
right_polygon_folder=os.path.join(right_folder,"right_polygon")
# 相対座標のlabelプログラム
# label関数の実行
label1(right_polygon_folder,right_folder)
right_label_folder=os.path.join(right_folder,"right_label")
# maxlabel関数の実行
maxlabel(right_label_folder,right_folder)
right_maxlabel_folder=os.path.join(right_folder,"right_maxlabel")

#ラベルをYolov8 のデータ形式に変換
maxlabel_change(right_maxlabel_folder)
right_maxlabel_change_folder = os.path.join(right_folder, 'maxlabel_change')
