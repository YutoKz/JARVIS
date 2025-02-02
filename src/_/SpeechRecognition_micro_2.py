"""
    マイクから音声を取得、テキスト変換
"""

import speech_recognition as sr

print("\n\n\n\n\n\n\n")
# システム上のマイクデバイスをリスト表示
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone {index}: {name}")
print("\n\n\n\n\n\n\n")

device_index = int(input())

# Recognizerオブジェクトを作成
recognizer = sr.Recognizer()

# マイクを使用して音声を取得
with sr.Microphone(device_index = device_index) as source:
    recognizer.adjust_for_ambient_noise(source, duration=1) # 環境音を1secキャリブレーション
    print("何か話してください...")
    audio_data = recognizer.listen(source)  # マイクからの音声を取得

# 認識結果を表示
try:
    text = recognizer.recognize_google(audio_data)
    print("認識されたテキスト: " + text)
except sr.UnknownValueError:
    print("音声が理解できませんでした")
except sr.RequestError:
    print("Google Speech Recognitionサービスに接続できませんでした")