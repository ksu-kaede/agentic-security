# example_load_env.py

import os
from dotenv import load_dotenv

# .envファイルを読み込む（カレントディレクトリの.envが対象）
load_dotenv()

# 環境変数を取得する
api_key = os.getenv("OPENAI_API_KEY")

print("読み込んだAPIキー:", api_key)

# 以降は api_key を使ってAPI呼び出しなどができる
