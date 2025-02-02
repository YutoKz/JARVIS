import pyaudio

# PyAudioのインスタンスを作成
pa = pyaudio.PyAudio()

# 使用可能な音声チャンネルの一覧を表示
for i in range(pa.get_device_count()):
    device_info = pa.get_device_info_by_index(i)
    print(device_info)

