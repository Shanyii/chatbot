# AI Chatbot 專案名稱

## 小組：第一組

### 組員：

* 組員1 : 楊姍頤
* 組員2 : 林瑞城

## 專案簡介

請簡要說明本專案的用途。
例如：本專案是一個使用 Streamlit 製作的 AI 聊天機器人，具備基本的對話與記憶功能。

## 目前功能
1.有聊天功能，並具備對話記憶
2.可以分析多種檔案(e.g.PDF、圖片(PNG/JPG)、TXT文字檔)
  使用者可以將檔案上傳並根據檔案內容提問
3.Web GUI 介面，使用 Streamlit 建立互動式網頁介面
4.對話紀錄自動儲存為JSON


## 執行方式

1. 下載專案
  ```bash
  git clone 你的專案網址
  ```
  進入專案資料夾
  ```bash
  cd chatbot
  ```
2. 安裝套件
   ```bash
   pip install streamlit langchain langchain-google-genai langchain-community python-dotenv pillow pypdf PyPDF2
   ```
3. 建立 .env
   ```bash
   GEMINI_API_KEY=AIzaSyBx8qcpQTBNphYZAjlP-Trm9foteWrhvWU
   ```
4. 啟動系統
   ```bash
   streamlit run chat_gemini_langchain.py
   ```
---

## 環境變數說明

請自行建立 `.env` 檔案，並填入自己的 API key。

範例：

```env
GEMINI_API_KEY=AIzaSyBx8qcpQTBNphYZAjlP-Trm9foteWrhvWU
```

## 遇到的問題與解法

### 問題 1

問題：執行程式時因找不到套件出現錯誤
解法：找到未安裝的套件並下載

### 問題 2

問題：解析 PDF 時出現錯誤
解法：安裝 PDF 相關套件

---

## 學習心得

透過本次專案，我們學習了如何將 大型語言模型（LLM）整合到實際應用中。
在開發過程中，我們不僅學會使用 LangChain 與 Gemini API 建立 AI Agent，也學會如何利用 Streamlit 快速建立 Web 介面。

此外，本專案也讓我們了解 多模態 AI 的應用方式，例如讓 AI 能夠分析 PDF 文件與圖片內容，並透過聊天方式與使用者互動。

在解決開發過程中的套件相依問題與 API 設定問題時，我們也更熟悉了 Python 環境管理與套件安裝流程。

這次專案讓我們對 AI 應用開發流程與系統整合有更深入的理解。

---

## GitHub 專案連結

楊姍頤
https://github.com/Shanyii/chatbot.git
