""" 対話形式で実行 """



import librosa
import soundfile as sf
import whisper
import pandas as pd
import noisereduce as nr
from pydub import AudioSegment
from pydub.effects import normalize
import librosa.effects


select = 1.5


"""
    # YouTubeから音声をDL
    yt-dlp -F https://www.youtube.com/live/VHi1sla6BFc
    yt-dlp -x --audio-format wav --audio-quality 0 -o "output" https://www.youtube.com/live/VHi1sla6BFc
"""


if select == 1:
    # 音声の前処理
    def preprocess_audio(input_file, output_file, target_sr=22050):
        y, sr = librosa.load(input_file, sr=None)
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        sf.write(output_file, y_resampled, target_sr)

    preprocess_audio("data/TTS/output.wav", "data/TTS/processed.wav")


elif select == 1.5:
    # 音声クレンジング
    # ノイズ除去
    def denoise_audio(input_file, output_file):
        y, sr = librosa.load(input_file, sr=None)
        reduced_noise = nr.reduce_noise(y=y, sr=sr)
        sf.write(output_file, reduced_noise, sr)

    denoise_audio("data/TTS/output.wav", "data/TTS/cleaned_audio.wav")

    # 音量正規化
    def normalize_audio(input_file, output_file):
        audio = AudioSegment.from_wav(input_file)
        normalized_audio = normalize(audio)
        normalized_audio.export(output_file, format="wav")

    normalize_audio("data/TTS/cleaned_audio.wav", "data/TTS/normalized_audio.wav")

    # 音声の分割
    def split_audio(input_file, output_prefix, min_silence_len=500, silence_thresh=-40):
        y, sr = librosa.load(input_file, sr=None)
        intervals = librosa.effects.split(y, top_db=30)
        
        for i, (start, end) in enumerate(intervals):
            sf.write(f"{output_prefix}_{i}.wav", y[start:end], sr)

    split_audio("data/TTS/normalized_audio.wav", "data/TTS/split_audio")

    # サンプリングレート統一
    def resample_audio(input_file, output_file, target_sr=22050):
        y, sr = librosa.load(input_file, sr=None)
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        sf.write(output_file, y_resampled, target_sr)

    resample_audio("data/TTS/split_audio_0.wav", "data/TTS/final_audio.wav")


    """
        yt-dlp --write-auto-sub --sub-lang ja --skip-download https://www.youtube.com/live/VHi1sla6BFc
    """


elif select == 2:
    # 自動字幕がない場合の文字おこし

    model = whisper.load_model("medium")
    result = model.transcribe("processed.wav", language="ja")
    print(result["text"])


elif select == 3:
    # 音声ファイルとテキストのリストを作成
    data = [
        ["0001.wav", "こんにちは、これはテストです。"],
        ["0002.wav", "このモデルは音声合成のために学習されました。"]
    ]

    df = pd.DataFrame(data, columns=["filename", "text"])
    df.to_csv("metadata.csv", index=False, sep="|")


elif select == 4:
    # 音声ファイルとテキストの対応付け
    