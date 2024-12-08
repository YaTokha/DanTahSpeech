import os
import subprocess
from pydub import AudioSegment

class Preprocess:
    def __init__(self, output_format="wav"):
        self.output_format = output_format

    def convert_to_wav(self, file_path: str, output_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        audio = AudioSegment.from_file(file_path)
        output_file = output_path or f"{os.path.splitext(file_path)[0]}.{self.output_format}"
        audio.export(output_file, format=self.output_format)
        return output_file

    def check_audio_duration(self, file_path: str) -> float:
        audio = AudioSegment.from_file(file_path)
        return len(audio) / 1000  # Длительность в секундах

    def reduce_noise(self, input_path: str, output_path: str) -> str:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Файл {input_path} не найден.")

        output_file = output_path or f"{os.path.splitext(input_path)[0]}_denoised.{self.output_format}"

        # Использование FFmpeg для подавления шума
        command = [
            "ffmpeg", "-i", input_path, "-af", "highpass=f=200, lowpass=f=3000",
            output_file
        ]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if not os.path.exists(output_file):
            raise RuntimeError("Не удалось подавить шум в аудиофайле.")

        return output_file

    def preprocess_audio(self, file_path: str, output_dir: str = "processed/") -> str:
        print("Шаг 1: Конвертация в WAV...")
        wav_file = self.convert_to_wav(file_path, os.path.join(output_dir, "converted.wav"))
        print(f"Конвертация завершена: {wav_file}")

        print("Шаг 2: Уменьшение шума...")
        denoised_file = self.reduce_noise(wav_file, os.path.join(output_dir, "denoised.wav"))
        print(f"Подавление шума завершено: {denoised_file}")

        return denoised_file
