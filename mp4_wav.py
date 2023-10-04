import os
import subprocess

def convert_mp4_to_wav(input_dir, output_dir):
    # 指定されたディレクトリ内のMP4ファイルを取得
    mp4_files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

    # WAVファイルのカウンタ
    wav_counter = 1

    for mp4_file in mp4_files:
        input_path = os.path.join(input_dir, mp4_file)
        output_name = f"setuna{wav_counter}.wav"
        output_path = os.path.join(output_dir, output_name)

        try:
            subprocess.run([
                'ffmpeg',
                '-i', input_path,
                '-acodec', 'pcm_s16le',
                '-ac', '1',
                '-ar', '44100',
                output_path
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
            print(f"変換成功: {input_path} -> {output_path}")
            wav_counter += 1
        except Exception as e:
            print(f"変換エラー: {input_path} -> {output_path} - {e}")

if __name__ == "__main__":
    input_directory = r'C:\Users\n22010\Desktop\AI\input'  # 入力ディレクトリを指定
    output_directory = r'C:\Users\n22010\Desktop\AI\output'  # 出力ディレクトリを指定

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    convert_mp4_to_wav(input_directory, output_directory)
