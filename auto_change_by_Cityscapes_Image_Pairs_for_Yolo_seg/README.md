# プログラムの概要

**auto_change_by_Cityscapes_Image_Pairs_for_Yolo_seg** は **[cityscapes-dataset](https://www.cityscapes-dataset.com/)** のデータセットを　　

**[Yolov8seg](https://docs.ultralytics.com/ja/tasks/segment/)** に対応するラベルに変換するためのプログラムです。　　

※**プログラムは _road_ のみのラベルを作成します。その他ラベルを作成したい場合はright_mask.py内のroad_color = np.arrayのRGB値を変更してください。**　　

RGB値に関する情報は個人で検索することをお願い申し上げます。　　

※うまく読み取れなかったラベルデータはnull_labelに保存されます。しかし、画像データはnull_imageのように処理されませんのでご注意ください。　　

# 使い方　　

## 1：**[Cityscapes Image Pairs](https://www.kaggle.com/datasets/dansbecker/cityscapes-image-pairs/data)** からデータセットをダウンロードします　　

## 2: 任意のフォルダを作成し、その中に1：でダウンロードした画像データを挿入します　　

※フォルダの階層は以下のようにしてください。　　

auto_change_by_Cityscapes_Image_Pairs_for_Yolo_seg/　　

├──任意のフォルダ　　

|    ├── 1.png　　

|    ├── 2.png　　

|    └── n.png　　

├── auto_data_remake.py　　

├── half_image.py　　

├── label1.py　　

├── label2.py　　

├── label3.py　　

├── right_mask.py　　

└── right_polygon.py　　

## 3: コマンドプロンプトなどで **auto_change_by_Cityscapes_Image_Pairs_for_Yolo_seg** に移動し、auto_data_remake.pyを実行してください　　

※実行中の表示　　

python auto_data_remake.py　　

分割処理したい画像フォルダのパスを教えてください：作成した任意のフォルダの名前を入力　　

全ての画像が処理されました。　　

処理が完了しました。マスク画像は data_remake\right\right_mask に保存されています。　　

処理が完了しました。polygon画像は data_remake\right\right_polygon に保存されています。　　

相対座標の抽出と保存が完了しました。保存先: data_remake\right\right_label　　

最大配列ID 21 のデータを以下のフォルダに保存しました： data_remake\right\right_maxlabel\91.txt　　

## 4: 元のデータと加工後のデータは **data_remake** に保存されます　　

※data_remakeは任意のフォルダと同じ階層に生成されます　　

# 解説　　

auto_change_by_Cityscapes_Image_Pairs_for_Yolo_seg/　　

├── 任意のフォルダ　　

├── data_remake　　

|       ├── right　　

|       |     ├── maxlabel_change　　

|       |     ├── null_label　　

|       |     ├── right_label　　

|       |     ├── right_mask　　

|       |     ├── right_maxlabel　　

|       |     └── right_polygon　　

|       └── left　　

├── auto_data_remake.py　　



## rightフォルダ　　

元の画像の右側半分に関する加工をしたフォルダを統括するフォルダ。　　

## maxlabel_changeフォルダ　　

最終的なラベルを保存したフォルダ。　　

完全なラベルデータ。　　

データは以下のように表現されている。　　

  
**
ID x1の座標 y1の座標 x2の座標 y2の座標・・・**　　

**0 0.4062 0.4375 0.4102 0.4414・・・**　　

このフォルダ内のtxtラベルをYoloに使用する。　　

  
## null_labelフォルダ　　

データのラベル化に失敗した場合に保存されるフォルダ。　　

## right_labelフォルダ　　

簡単なラベル処理。不完全。　　

## right_maskフォルダ　　

二値化処理後の画像を保存するフォルダ。　　

RGB値からデータを絞り、対象物を白色で表現。その他は黒色。　　

## right_maxlabelフォルダ　　

**right_label**で処理されたのち、**最も配列サイズの大きいラベル**を抽出したtxtファイルを保存するフォルダ。　　

## right_polygonフォルダ　　

ポリゴン処理後の画像を保存するフォルダ。　　

## leftフォルダ　　

分割後、加工されていない画像を保存するフォルダ。　　

Yolo学習時のimagesに用いる。　　

