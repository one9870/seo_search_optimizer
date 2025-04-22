import tkinter as tk
from tkinter import messagebox
import threading
import time
import webbrowser
import random
import urllib.parse

# 關鍵字搜尋間隔時間（秒）
SEARCH_INTERVAL = 300  # 5 分鐘

# 使用的搜尋引擎網址（以 google.com.tw 為主）
GOOGLE_SEARCH_URL = "https://www.google.com.tw/search?q={query}"

# 紀錄是否正在執行
is_running = False

# 背景執行的搜尋函式
def start_search_loop(keywords):
    global is_running
    is_running = True
    while is_running:
        keyword = random.choice(keywords)  # 隨機選一個關鍵字
        encoded = urllib.parse.quote(keyword)
        url = GOOGLE_SEARCH_URL.format(query=encoded)
        webbrowser.open(url, new=0)  # 開啟預設瀏覽器新分頁
        print(f"已搜尋關鍵字：{keyword}")
        time.sleep(SEARCH_INTERVAL)

def stop_search():
    global is_running
    is_running = False
    print("已停止搜尋。")

# GUI 主程式
def run_gui():
    def on_start():
        keyword_text = keyword_entry.get("1.0", tk.END).strip()
        if not keyword_text:
            messagebox.showwarning("提示", "請輸入至少一個關鍵字")
            return
        keywords = [k.strip() for k in keyword_text.split("\n") if k.strip()]
        start_btn.config(state="disabled")
        stop_btn.config(state="normal")
        threading.Thread(target=start_search_loop, args=(keywords,), daemon=True).start()

    def on_stop():
        stop_search()
        start_btn.config(state="normal")
        stop_btn.config(state="disabled")

    root = tk.Tk()
    root.title("SEO優化神器")
    root.geometry("400x300")

    tk.Label(root, text="請輸入關鍵字（每行一個）:").pack(pady=10)
    keyword_entry = tk.Text(root, height=10, width=40)
    keyword_entry.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    start_btn = tk.Button(btn_frame, text="開始搜尋", command=on_start)
    start_btn.grid(row=0, column=0, padx=10)

    stop_btn = tk.Button(btn_frame, text="停止執行", command=on_stop, state="disabled")
    stop_btn.grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    run_gui()