import time
from pathlib import Path
import os
import ast

def maxlabel(right_label_folder, right_folder):
    maxlabels_folder = Path(os.path.join(right_folder, "right_maxlabel"))
    null_label_folder = Path(os.path.join(right_folder, "null_label"))
    
    maxlabels_folder.mkdir(parents=True, exist_ok=True)
    null_label_folder.mkdir(parents=True, exist_ok=True)

    for txt_file in os.listdir(right_label_folder):
        if txt_file.endswith('.txt'):
            file_path = os.path.join(right_label_folder, txt_file)

            try:
                with open(file_path, 'r') as file:
                    data = {}
                    for line in file:
                        if ':' in line:
                            key, value = line.split(':')
                            data[int(key)] = ast.literal_eval(value.strip())

                    if data:
                        max_id = max(data, key=lambda k: len(data[k]))
                        output_file_path = maxlabels_folder / txt_file
                        with open(output_file_path, 'w') as file:
                            file.write(f"{max_id}: {data[max_id]}")
                        print(f"最大配列ID {max_id} のデータを以下のフォルダに保存しました： {output_file_path}")
                    else:
                        raise ValueError("No valid data")
            except (ValueError, IOError):
                null_file_path = null_label_folder / txt_file
                time.sleep(1)  # 少し待ってからファイル操作を試みる
                os.rename(file_path, null_file_path)
                print(f"次のファイル内にデータが見つかりませんでした： {txt_file}. データの無いファイルの保存先： {null_file_path}.")
