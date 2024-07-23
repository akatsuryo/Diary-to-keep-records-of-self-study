# 仕様に基づいてプログラムを修正するためのコード
import os
import re

def maxlabel_change(directory):
    # 出力ディレクトリのパス
    output_directory = os.path.join(directory, '../maxlabel_change')
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # ファイルをディレクトリから読み込む
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        with open(file_path, 'r') as file:
            data = file.read()
        
        # ラベルの変更 ('任意の数字:' を 'roadのID：0' に変更)
        new_data = re.sub(r'\d+:', '0', data)
        
        # 座標の形式変更 ('[(x, y), (x, y), ...]' を 'x y x y ...' に変更)
        new_data = new_data.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "")
        
        # 新しいファイル名を生成
        new_filename = f"{filename}"
        new_file_path = os.path.join(output_directory, new_filename)
        
        # 変更されたデータを新しいファイルに書き込む
        with open(new_file_path, 'w') as file:
            file.write(new_data)

# このコードはローカル環境での実行が必要です。
