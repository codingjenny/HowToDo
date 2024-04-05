import os
from openai import OpenAI

# api_key 已經設置成環境變數，並從環境變數取得 api_key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# 設定 api_key，讓 client 這個變數知道是在使用哪個 api
client = OpenAI(api_key=api_key)

# 測試 openai_api
try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Translate 'How are you?' to Chinese.",
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens = 50
    )
    print(chat_completion)
except Exception as e:
    print(f"An error occurred: {e}")