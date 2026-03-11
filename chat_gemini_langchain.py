# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image
import io, os, json
from datetime import datetime
from google import genai
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="AI 多模態助手", layout="wide")

if not api_key:
    st.error("❌ 請在 .env 檔案中設定 GEMINI_API_KEY")
    st.stop()

# 初始化 Gemini Client
client = genai.Client(api_key=api_key)

# 初始化 session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "json_file" not in st.session_state:
    st.session_state.json_file = "chat_history.json"

# 側邊欄功能
with st.sidebar:
    st.header("功能區")
    uploaded_file = st.file_uploader(
        "上傳圖片/PDF/文字檔", 
        type=["png", "jpg", "jpeg", "pdf", "txt"]
    )
    if st.button("清除對話"):
        st.session_state.messages = []
        st.experimental_rerun()

# 顯示已上傳檔案
if uploaded_file:
    st.markdown("**已上傳檔案：**")
    if uploaded_file.type.startswith("image/"):
        st.image(uploaded_file, use_column_width=True)
    elif uploaded_file.type == "application/pdf":
        st.write("PDF 檔案已上傳，可解析內容。")
    elif uploaded_file.type == "text/plain":
        st.text(uploaded_file.getvalue().decode())

# 顯示歷史訊息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 聊天輸入
if prompt := st.chat_input("輸入訊息..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            # 準備 contents
            contents = [prompt]  # 文字必須是 str

            # 處理圖片
            if uploaded_file:
                if uploaded_file.type.startswith("image/"):
                    img = Image.open(uploaded_file)
                    contents.append(img)  # 直接傳 PIL.Image.Image
                elif uploaded_file.type == "application/pdf":
                    from PyPDF2 import PdfReader
                    reader = PdfReader(uploaded_file)
                    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
                    contents.append(pdf_text)
                elif uploaded_file.type == "text/plain":
                    text_content = uploaded_file.getvalue().decode()
                    contents.append(text_content)

            # 呼叫 Gemini 生成回應
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents
            )
            output = response.text if hasattr(response, "text") else response.result[0].content
            st.write(output)

            # 更新 session_state
            st.session_state.messages.append({"role": "assistant", "content": output})

            # 即時存成 JSON
            with open(st.session_state.json_file, "w", encoding="utf-8") as f:
                json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)

        except Exception as e:
            st.error(f"連線出錯: {e}")