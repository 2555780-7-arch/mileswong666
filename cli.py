from google import genai

# 1. 綁定你的通行證
client = genai.Client(api_key="AIzaSyAB8FWtDT3uZpW8rHMStL4AesZcHqouI30")

print("--- Gemini 3.1 Pro 已連線 (輸入 'q' 退出) ---")

# 2. 開始對話循環
while True:
    user_input = input("你: ")
    if user_input.lower() == 'q':
        break
    
    # 3. 調用最強模型
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents=user_input
    )
    print(f"Gemini: {response.text}\n")