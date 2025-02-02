import re
import os
from tkinter import Label, Canvas

class Markdown2Tkinter:
    def __init__(self, markdown_text, frame):
        self.markdown2Tkinter(markdown_text, frame)

    def markdown2Tkinter(self, markdown_text, frame):
            # markdown形式のテキストの読み込み
            text = markdown_text

            # textを改行で分割
            text = text.split('\n')

            tkObject = []

            # textを1行ずつlineMdToTkinterに渡す
            for line in text:
                tkObject.append(self.line2Tkinter(line, frame))

            # tkObjectの要素を1つずつframeに追加
            for i in tkObject:
                i.pack(anchor="nw")

    def line2Tkinter(self, line, frame):
         # 構造化パターンマッチングを使って、textを解析
        match StrRe(line):
            # lineが#+半角スペースで始まる場合
            case "#+ ":
                # lineが#で始まる場合、#の数を取得
                count = line.count("#")

                # lineから#を削除
                line = line.replace("#", "")

                # lineの前後の空白を削除
                line = line.strip()

                # labelを作成
                label = Label(frame, text=line, font=("Noto Sans CJK JP", 15 + (6 - count) *3), justify="left")
                return label
            
            # lineが半角スペース*+*+半角スペースで始まる場合
            case "^ *\* ":
                # lineが*で始まる場合、*を・に置換
                line = line.replace("*", "・")

                # labelを作成
                label = Label(frame, text=line, font=("Noto Sans CJK JP", 15), justify="left")
                return label

            case "---":
                # lineが---で始まる場合、lineを作成
                canvas = Canvas(frame, width=500, height=1, background="gray30", highlightthickness=0)
                return canvas

            case r"!\[":
                # lineが![で始まる場合、()の中身を取得
                line = re.findall(r'\((.*?)\)', line)[0].replace(".\\", "")
                line = os.path.join(os.path.dirname(__file__), line)

                # lineから画像を読み込み
                readImage = Image.open(line)
                global image
                image = ImageTk.PhotoImage(readImage)

                # canvasを作成
                canvas = Canvas(frame, width=readImage.width, height=readImage.height, highlightthickness=0)

                # canvasに画像を描画
                canvas.create_image(0, 0, image=image, anchor="nw")
                return canvas

            case _:
                # labelを作成
                label = Label(frame, text=line, font=("Noto Sans CJK JP", 15), justify="left")
                return label

class StrRe(str):
    def __init__(self, var):
        self.var = var
        pass

    def __eq__(self, pattern):
        return True if re.search(pattern, self.var) is not None else False

global image