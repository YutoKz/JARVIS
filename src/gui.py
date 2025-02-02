"""

import tkinter as tk

def update_input():
    text = input_entry.get()
    current_text = input_var.get()
    new_text = current_text + "\n" + text if current_text else text
    input_var.set(new_text)
    input_entry.delete(0, tk.END)

def submit_text():
    text = input_var.get()
    output_var.set(text)

def clear_text():
    input_var.set("")
    input_entry.delete(0, tk.END)

# ウィンドウの作成
root = tk.Tk()
root.title("テキスト表示アプリ")
root.geometry("400x250")

# 実際の入力用フィールド (左上)
input_entry = tk.Entry(root, width=30)
input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用フィールド (左上下)
input_var = tk.StringVar()
input_label = tk.Entry(root, width=30, textvariable=input_var, state="readonly")
input_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力フィールド (右上)
output_var = tk.StringVar()
output_label = tk.Entry(root, width=30, textvariable=output_var, state="readonly")
output_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# 入力ボタン (左下)
button_update = tk.Button(root, text="入力", command=update_input)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 提出ボタン (左下)
button_submit = tk.Button(root, text="提出", command=submit_text)
button_submit.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="削除", command=clear_text)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# メインループ
root.mainloop()
"""

"""
import tkinter as tk
import tkinter.scrolledtext as st

def update_input():
    text = input_entry.get()
    current_text = input_var.get()
    new_text = current_text + "\n" + text if current_text else text
    input_var.set(new_text)
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, new_text)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

def submit_text():
    text = input_var.get()
    output_var.set(text)
    output_display.configure(state="normal")
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, text)
    output_display.configure(state="disabled")

def clear_text():
    input_var.set("")
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

# ウィンドウの作成
root = tk.Tk()
root.title("テキスト表示アプリ")
root.geometry("500x300")

# 実際の入力用フィールド (左上)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用テキストエリア (左下)
input_var = tk.StringVar()
input_display = st.ScrolledText(root, width=40, height=5, state="disabled")
input_display.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力表示用テキストエリア (右下)
output_var = tk.StringVar()
output_display = st.ScrolledText(root, width=40, height=5, state="disabled")
output_display.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# 入力ボタン (左下)
button_update = tk.Button(root, text="入力", command=update_input)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 提出ボタン (左下)
button_submit = tk.Button(root, text="提出", command=submit_text)
button_submit.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="削除", command=clear_text)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# メインループ
root.mainloop()
"""

"""
import tkinter as tk
import tkinter.scrolledtext as st

def update_input():
    text = input_entry.get()
    current_text = input_var.get()
    new_text = current_text + "\n" + text if current_text else text
    input_var.set(new_text)
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, new_text)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

def submit_text():
    text = input_var.get()
    output_var.set(text)
    output_display.configure(state="normal")
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, text)
    output_display.configure(state="disabled")

def clear_text():
    input_var.set("")
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

# ウィンドウの作成
root = tk.Tk()
root.title("テキスト表示アプリ")
root.geometry("800x300")

# 実際の入力用フィールド (左上)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用テキストエリア (左下)
input_var = tk.StringVar()
input_display = st.ScrolledText(root, width=50, height=8, state="disabled")
input_display.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力表示用テキストエリア (右下)
output_var = tk.StringVar()
output_display = st.ScrolledText(root, width=50, height=8, state="disabled")
output_display.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# 入力ボタン (左下)
button_update = tk.Button(root, text="入力", command=update_input)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 提出ボタン (左下)
button_submit = tk.Button(root, text="提出", command=submit_text)
button_submit.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="削除", command=clear_text)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# メインループ
root.mainloop()
"""


""" 今んとこ１番

import tkinter as tk
import tkinter.scrolledtext as st

def update_input():
    text = input_entry.get()
    current_text = input_var.get()
    new_text = current_text + "\n" + text if current_text else text
    input_var.set(new_text)
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, new_text)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

def submit_text():
    text = input_var.get()
    output_var.set(text)
    output_display.configure(state="normal")
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, text)
    output_display.configure(state="disabled")

def clear_text():
    input_var.set("")
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

# ウィンドウの作成
root = tk.Tk()
root.title("テキスト表示アプリ")
root.geometry("800x300")

# 実際の入力用フィールド (左上)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用テキストエリア (左下)
input_var = tk.StringVar()
input_display = st.ScrolledText(root, width=50, height=15, state="disabled")
input_display.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力表示用テキストエリア (右下)
output_var = tk.StringVar()
output_display = st.ScrolledText(root, width=50, height=15, state="disabled")
output_display.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# 入力ボタン (左下)
button_update = tk.Button(root, text="入力", command=update_input)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 提出ボタン (左下)
button_submit = tk.Button(root, text="提出", command=submit_text)
button_submit.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="削除", command=clear_text)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# メインループ
root.mainloop()
"""






""" ベース
import tkinter as tk
import tkinter.scrolledtext as st
import markdown2tkinter as md2tk

def update_input():
    text = input_entry.get()
    current_text = input_var.get()
    new_text = current_text + "\n" + text if current_text else text
    input_var.set(new_text)
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, new_text)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)

def submit_text():
    text = input_var.get()
    output_var.set(text)
    output_display.configure(state="normal")
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, text)
    output_display.configure(state="disabled")

    for widget in bottom_frame.winfo_children():
        widget.destroy()
    md2tk.Markdown2Tkinter(output_var.get(), bottom_frame)

def clear_text():
    input_var.set("")
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.configure(state="disabled")
    input_entry.delete(0, tk.END)


# ウィンドウの作成
root = tk.Tk()
root.title("テキスト表示アプリ")
root.geometry("800x1000")

# 実際の入力用フィールド (左上)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用テキストエリア (左下)
input_var = tk.StringVar()
input_display = st.ScrolledText(root, width=50, height=10, state="disabled")
input_display.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力表示用テキストエリア (右下)
output_var = tk.StringVar()
output_display = st.ScrolledText(root, width=50, height=10, state="disabled")
output_display.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# 入力ボタン (左下)
button_update = tk.Button(root, text="入力", command=update_input)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 提出ボタン (左下)
button_submit = tk.Button(root, text="提出", command=submit_text)
button_submit.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="削除", command=clear_text)
button_clear.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# 空のフレーム (一番下)
bottom_frame = tk.Frame(root, height=20)
bottom_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")


# メインループ
root.mainloop()
"""




# 本番
import tkinter as tk
import tkinter.scrolledtext as st
import utils.markdown2tkinter as md2tk
import speech_recognition as sr
import google.generativeai as genai
from llm.api_key_list import GEMINI_API_KRY
from IPython.display import Markdown
import textwrap

device_index = int(input("マイク番号(-1: SHOW LIST): "))
while device_index == -1:
    # システム上のマイクデバイスをリスト表示
    print("---------------------------Microphone List-----------------------------")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone {index}: {name}")
    print("-----------------------------------------------------------------------")
    device_index = int(input("マイク番号(-1: SHOW LIST): ")) 

# Recognizerオブジェクトを作成
recognizer = sr.Recognizer()

def speech2text():
    # マイクを使用して音声を取得
    with sr.Microphone(device_index = device_index) as source:
        #recognizer.adjust_for_ambient_noise(source, duration=1) # 環境音を1secキャリブレーション
        print("質問をどうぞ！")
        audio_data = recognizer.listen(source)  # マイクからの音声を取得

    # 認識結果を表示
    try:
        text = recognizer.recognize_google(audio_data, language='ja-JP')
        print("認識されたテキスト: " + text)
    except sr.UnknownValueError:
        text = ""
        print("音声が理解できませんでした")
    except sr.RequestError:
        text = ""
        print("Google Speech Recognitionサービスに接続できませんでした")
    
    return text

def ask_gemini(query_text):
    query_text = query_text + "\n(なお、出力は読み上げる原稿にする予定のため、markdown形式にする必要はありません。原稿としてそのまま読み上げても不自然にならないような回答を心がけなさい。)"
    genai.configure(api_key=GEMINI_API_KRY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    responce = model.generate_content(query_text)
    responce_text = responce.text
    print("-----------------")
    print(query_text)
    print("-----------------")
    print(responce.text)
    print("-----------------")

    return responce_text


def update_query():
    #text = input_entry.get()
    text = speech2text()
    current_text = input_var.get()
    new_text = current_text + " " + text if current_text else text
    input_var.set(new_text)
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.insert(tk.END, new_text)
    input_display.configure(state="disabled")
    #input_entry.delete(0, tk.END)

def submit_text():
    query = input_var.get()

    #output_var.set(text) 
    answer = ask_gemini(query) # gemini
    
    output_display.configure(state="normal")
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, answer)
    output_display.configure(state="disabled")

    #for widget in bottom_frame.winfo_children():
    #    widget.destroy()
        ##md2tk.Markdown2Tkinter(output_var.get(), bottom_frame) 
    #md2tk.Markdown2Tkinter(answer, bottom_frame)

def clear_text():
    input_var.set("")
    input_display.configure(state="normal")
    input_display.delete("1.0", tk.END)
    input_display.configure(state="disabled")
    #input_entry.delete(0, tk.END)


# ウィンドウの作成
root = tk.Tk()
root.title("J.A.R.V.I.S.")
root.geometry("800x600")

    # 実際の入力用フィールド (左上)
    #input_entry = tk.Entry(root, width=50)
    #input_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# 入力表示用テキストエリア (左下)
input_var = tk.StringVar()
input_display = st.ScrolledText(root, width=50, height=30, state="disabled")
input_display.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 出力表示用テキストエリア (右下)
output_var = tk.StringVar()
output_display = st.ScrolledText(root, width=50, height=30, state="disabled")
output_display.grid(row=1, column=1, padx=10, pady=5, sticky="e")

# ボタンフレーム
frame_query_button = tk.Frame(root)
frame_query_button.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

# 入力ボタン (左端)
button_update = tk.Button(frame_query_button, text="Speek", command=update_query)
button_update.pack(side="left", padx=5)

# 提出ボタン (入力ボタンの右隣)
button_clear = tk.Button(frame_query_button, text="Clear", command=clear_text)
button_clear.pack(side="left", padx=5)
"""
# 入力ボタン (左下)
button_update = tk.Button(root, text="Speek", command=update_query)
button_update.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# 削除ボタン (右下)
button_clear = tk.Button(root, text="Clear", command=clear_text)
button_clear.grid(row=3, column=0, padx=10, pady=10, sticky="w")
"""

# 提出ボタン (左下)
button_submit = tk.Button(root, text="Submit->LLM", command=submit_text)
button_submit.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# 空のフレーム (一番下)
# markdownで出力を表示しようとしていたが、うまくいかなかったのでコメントアウト
#bottom_frame = tk.Frame(root, height=20)
#bottom_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")


# メインループ
root.mainloop()