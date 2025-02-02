# Project Jarvis

https://qiita.com/K2_ML/items/2804594454b39180c909

## 処理の流れ

- start ボタンを押して音声入力を開始
- 入力した音声を認識・テキストフィールドに表示
- 足りなければ再度入力により追加可能
- 質問が完成したら submit ボタンを押して chatgpt apiに送信
- LLMの出力を出力テキストフィールドに表示 + 好きな音声で出力
- （次の質問時）前の質問を clear 、最初から繰り返す

## 必要なGUIコンポーネント

- 入力テキストフィールド
- 出力テキストフィールド
- 収録 start ボタン
- 質問 submit ボタン
- 入力の clear ボタン
- (マイクの番号を変更するリスト)

## メモ

- custom tkinterというのがあるらしい [参考](https://zenn.dev/foxfoxfox/articles/be23e942cf3192)
- 今llmへの質問をgeminiの公式apiでやってるが、langchainなら過去の履歴込みでの実装が楽にできんじゃね
- 特定の人物に読み上げさせるタスク
  - voice cloning
  - **音声合成 TTS**
  - voice conversion
- TTSの実装ライブラリ
  - Coqui TTSに決定, Tortoise-TTSは高精度だが学習推論コスト高そう
- TTSの学習データ
  - クレンジング周りがやりにくいので、データ準備はWSLのProject/try, tmp1で
  - spleeterでBGM除去、10分ごとしかできない？ので10minでwavを区切ってそれぞれvocal抽出
  - 音声データを無音で区切る
  - 区切ったデータそれぞれをwhisperで認識
  - アノテーションcsvに
  - 次
    - いよいよ学習

## 課題

- 音声入力時、話し終えたらすぐ入力を終わりたい。今は待ちが発生
- 会話の履歴を考慮できてない。LangChainなら楽に実装？
