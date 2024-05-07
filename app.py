import pandas as pd
import os
import shutil

# 指定フォルダのパス
base_folder_path = 'path_to_your_base_folder'

# CSVファイルのパス
csv_path = 'input.csv'

# 出力ディレクトリのパス
output_directory = 'output'

# 既存の出力ディレクトリがあれば削除
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)

# 出力ディレクトリを作成
os.makedirs(output_directory)

# CSVファイルを読み込む
df = pd.read_csv(csv_path)

# ファイルのコピーを行う
for index, row in df.iterrows():
    relative_path = row['relative_path']
    source_path = os.path.join(base_folder_path, relative_path)
    destination_path = os.path.join(output_directory, relative_path)
    
    # コピー先のディレクトリが存在しない場合は作成
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # ファイルをコピー
    shutil.copy2(source_path, destination_path)
    
    print(f'Copied from {source_path} to {destination_path}')

print('All files have been copied successfully.')
